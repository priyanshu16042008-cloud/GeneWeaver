import time

from src.sequence_alignment import global_align

def generate_sequence(length):
    bases = "ATGC"
    return "".join(bases[i % 4] for i in range(length))

def run_benchmark():
    print("GeneWeaver Performance Benchmark")
    print("-" * 40)

    for length in [50, 100, 200, 400]:
        seq1 = generate_sequence(length)
        seq2 = generate_sequence(length)

        start = time.perf_counter()
        result = global_align(seq1, seq2)
        end = time.perf_counter()

        elapsed = (end - start) * 1000

        print(
            f"Length: {length} | "
            f"Time: {elapsed:.3f} ms | "
            f"Score: {result['score']}"
        )

if __name__ == "__main__":
    run_benchmark()