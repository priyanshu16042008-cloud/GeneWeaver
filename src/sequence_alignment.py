
def validate_sequence(sequence):
    """
    Validate a DNA sequence.
    Only A, T, G and C are allowed.
    """

    if not isinstance(sequence, str):
        raise TypeError("DNA sequence must be a string.")

    if not sequence:
        raise ValueError("DNA sequence cannot be empty.")

    sequence = sequence.upper()

    invalid_bases = set(sequence) - {"A", "T", "G", "C"}

    if invalid_bases:
        raise ValueError(
            f"Invalid DNA characters: {invalid_bases}"
        )

    return sequence

def validate_scoring_parameters(match, mismatch, gap):
    """
    Validate scoring parameters.
    All scoring values must be integers.
    """

    parameters = {
        "match": match,
        "mismatch": mismatch,
        "gap": gap
    }

    for name, value in parameters.items():
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(
                f"{name} score must be an integer."
            )

    if match <= 0:
        raise ValueError("Match score must be positive.")

    if mismatch >= 0:
        raise ValueError("Mismatch score must be negative.")

    if gap >= 0:
        raise ValueError("Gap penalty must be negative.")

def global_align(seq1, seq2, match=2, mismatch=-1, gap=-2):
    """
    Perform global DNA sequence alignment using
    the Needleman-Wunsch algorithm.
    """

    validate_scoring_parameters(match, mismatch, gap)

    seq1 = validate_sequence(seq1)
    seq2 = validate_sequence(seq2)

    rows = len(seq1) + 1
    cols = len(seq2) + 1

    # Initialize scoring matrix
    matrix = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        matrix[i][0] = i * gap

    for j in range(cols):
        matrix[0][j] = j * gap

    # Fill scoring matrix
    for i in range(1, rows):
        for j in range(1, cols):

            if seq1[i - 1] == seq2[j - 1]:
                diagonal = matrix[i - 1][j - 1] + match
            else:
                diagonal = matrix[i - 1][j - 1] + mismatch

            up = matrix[i - 1][j] + gap
            left = matrix[i][j - 1] + gap

            matrix[i][j] = max(diagonal, up, left)

    # Traceback
    aligned_seq1 = []
    aligned_seq2 = []

    i = len(seq1)
    j = len(seq2)

    while i > 0 or j > 0:

        if i > 0 and j > 0:
            score = match if seq1[i - 1] == seq2[j - 1] else mismatch

            if matrix[i][j] == matrix[i - 1][j - 1] + score:
                aligned_seq1.append(seq1[i - 1])
                aligned_seq2.append(seq2[j - 1])
                i -= 1
                j -= 1
                continue

        if i > 0 and matrix[i][j] == matrix[i - 1][j] + gap:
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append("-")
            i -= 1
        else:
            aligned_seq1.append("-")
            aligned_seq2.append(seq2[j - 1])
            j -= 1

    return {
        "aligned_seq1": "".join(reversed(aligned_seq1)),
        "aligned_seq2": "".join(reversed(aligned_seq2)),
        "score": matrix[-1][-1]
    }
