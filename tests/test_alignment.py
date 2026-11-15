
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

    def test_lowercase_sequences(self):
        result = global_align("atgc", "ATGC")
        self.assertEqual(result["score"], 8)


    def test_invalid_dna_sequence(self):
        with self.assertRaises(ValueError):
            global_align("ATGX", "ATGC")


    def test_invalid_character_in_second_sequence(self):
        with self.assertRaises(ValueError):
            global_align("ATGC", "ATGN")


if __name__ == "__main__":
    unittest.main()
