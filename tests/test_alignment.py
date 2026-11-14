
import unittest

from src.sequence_alignment import global_align


class TestGlobalAlignment(unittest.TestCase):

    def test_identical_sequences(self):
        result = global_align("ATGC", "ATGC")
        self.assertEqual(result["aligned_seq1"], "ATGC")
        self.assertEqual(result["aligned_seq2"], "ATGC")
        self.assertEqual(result["score"], 8)

    def test_different_sequences(self):
        result = global_align("AAAA", "TTTT")
        self.assertEqual(result["score"], -4)

    def test_empty_sequence(self):
        result = global_align("", "ATGC")
        self.assertEqual(result["aligned_seq1"], "----")
        self.assertEqual(result["aligned_seq2"], "ATGC")
        self.assertEqual(result["score"], -8)

    def test_alignment_lengths(self):
        result = global_align("ATGC", "AGC")
        self.assertEqual(
            len(result["aligned_seq1"]),
            len(result["aligned_seq2"])
        )


if __name__ == "__main__":
    unittest.main()
