
import unittest

from geneweaver.sequence import normalize_dna_sequence


class TestNormalizeDNASequence(unittest.TestCase):

    def test_valid_uppercase_sequence(self):
        self.assertEqual(
            normalize_dna_sequence("ATGCGA"),
            "ATGCGA"
        )

    def test_lowercase_sequence(self):
        self.assertEqual(
            normalize_dna_sequence("atgcga"),
            "ATGCGA"
        )

    def test_sequence_with_whitespace(self):
        self.assertEqual(
            normalize_dna_sequence(" atg cga "),
            "ATGCGA"
        )

    def test_empty_sequence(self):
        with self.assertRaises(ValueError):
            normalize_dna_sequence("")

    def test_whitespace_only_sequence(self):
        with self.assertRaises(ValueError):
            normalize_dna_sequence("   ")

    def test_invalid_dna_character(self):
        with self.assertRaises(ValueError):
            normalize_dna_sequence("ATGX")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            normalize_dna_sequence(123)


if __name__ == "__main__":
    unittest.main()
