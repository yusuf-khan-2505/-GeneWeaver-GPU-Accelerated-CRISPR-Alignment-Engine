import unittest

from geneweaver.sequence import (
    find_exact_match,
    gc_content_percentage,
    normalize_dna_sequence,
    reverse_complement,
)


class TestNormalizeDNASequence(unittest.TestCase):
    def test_valid_uppercase_sequence(self):
        self.assertEqual(normalize_dna_sequence("ATGCGA"), "ATGCGA")

    def test_lowercase_sequence(self):
        self.assertEqual(normalize_dna_sequence("atgcga"), "ATGCGA")

    def test_sequence_with_whitespace(self):
        self.assertEqual(normalize_dna_sequence(" atg cga "), "ATGCGA")

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


class TestFindExactMatch(unittest.TestCase):
    def test_returns_first_zero_based_position(self):
        self.assertEqual(find_exact_match("ACGTAC", "GTA"), 2)

    def test_returns_minus_one_when_absent(self):
        self.assertEqual(find_exact_match("ACGTAC", "GGG"), -1)

    def test_normalizes_case_and_whitespace(self):
        self.assertEqual(find_exact_match("ac gtac", " gT a "), 2)

    def test_match_at_start(self):
        self.assertEqual(find_exact_match("ACGTAC", "ACG"), 0)

    def test_match_at_end(self):
        self.assertEqual(find_exact_match("ACGTAC", "TAC"), 3)


if __name__ == "__main__":
    unittest.main()
