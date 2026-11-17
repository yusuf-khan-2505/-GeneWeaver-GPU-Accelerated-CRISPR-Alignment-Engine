
"""DNA sequence validation utilities."""


VALID_BASES = {"A", "T", "G", "C"}


def normalize_dna_sequence(sequence: str) -> str:
    """Normalize and validate a DNA sequence."""

    if not isinstance(sequence, str):
        raise TypeError("DNA sequence must be a string.")

    normalized = "".join(sequence.split()).upper()

    if not normalized:
        raise ValueError("DNA sequence cannot be empty.")

    invalid_bases = set(normalized) - VALID_BASES

    if invalid_bases:
        raise ValueError(
            f"Invalid DNA bases found: {sorted(invalid_bases)}"
        )

    return normalized


def gc_content_percentage(sequence: str) -> float:
    """Return the percentage of bases in a DNA sequence that are G or C."""

    normalized = normalize_dna_sequence(sequence)
    gc_count = normalized.count("G") + normalized.count("C")

    return gc_count / len(normalized) * 100


def reverse_complement(sequence: str) -> str:
    """Return the reverse complement of a DNA sequence."""

    normalized = normalize_dna_sequence(sequence)

    complement_table = str.maketrans("ATGC", "TACG")

    return normalized.translate(complement_table)[::-1]

def find_exact_match(sequence: str, pattern: str) -> int:
    """Return the first zero-based position of pattern, or -1 if absent."""

    normalized_sequence = normalize_dna_sequence(sequence)
    normalized_pattern = normalize_dna_sequence(pattern)

    return normalized_sequence.find(normalized_pattern)


def find_exact_match(sequence: str, pattern: str) -> int:
    """Return the first zero-based position of pattern, or -1 if absent."""

    normalized_sequence = normalize_dna_sequence(sequence)
    normalized_pattern = normalize_dna_sequence(pattern)

    return normalized_sequence.find(normalized_pattern)
