# Determine the RNA complement of a given DNA sequence.
#
# Both DNA and RNA strands are a sequence of nucleotides.
#
# The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).
#
# The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).
#
# Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:
#
# G -> C
# C -> G
# T -> A
# A -> U


def to_rna(dna_strand: str) -> str:
    if len(dna_strand) == 0:
        return ""
    else:
        complement = ""
        for nucleotide in dna_strand.upper():
            match nucleotide:
                case "G":
                    complement += "C"
                case "C":
                    complement += "G"
                case "T":
                    complement += "A"
                case "A":
                    complement += "U"
                case _:
                    complement += ""
    return complement