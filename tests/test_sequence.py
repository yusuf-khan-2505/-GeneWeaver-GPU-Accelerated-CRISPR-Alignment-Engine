
import unittest

from geneweaver.sequence import (
    gc_content_percentage,
    normalize_dna_sequence,
    reverse_complement,
)


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


class TestGCContentPercentage(unittest.TestCase):

    def test_calculates_gc_percentage(self):
        self.assertEqual(gc_content_percentage("ATGC"), 50.0)

    def test_normalizes_sequence_before_calculation(self):
        self.assertEqual(gc_content_percentage(" g c a "), 66.66666666666666)

class TestReverseComplement(unittest.TestCase):

    def test_reverse_complement(self):
        self.assertEqual(reverse_complement("ATGC"), "GCAT")

    def test_lowercase_sequence(self):
        self.assertEqual(reverse_complement("atgc"), "GCAT")

    def test_sequence_with_whitespace(self):
        self.assertEqual(reverse_complement("AT G C"), "GCAT")

    def test_invalid_sequence(self):
        with self.assertRaises(ValueError):
            reverse_complement("ATGX")

if __name__ == "__main__":
    unittest.main()
