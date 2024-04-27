def proteins(strand: str) -> list:
    prot = []
    if len(strand) % 3 == 0:
        strands = [strand[i:i + 3] for i in range(0, len(strand), 3)]
    for single_strand in strands:
        if "AUG" in single_strand:
            prot.append("Methionine")
        if "UUU" in single_strand:
            prot.append("Phenylalanine")
        if "UUC" in single_strand:
            prot.append("Phenylalanine")
        if "UUA" in single_strand:
            prot.append("Leucine")
        if "UUG" in single_strand:
            prot.append("Leucine")
        if "UCU" in single_strand:
            prot.append("Serine")
        if "UCC" in single_strand:
            prot.append("Serine")
        if "UCA" in single_strand:
            prot.append("Serine")
        if "UCG" in single_strand:
            prot.append("Serine")
        if "UAU" in single_strand:
            prot.append("Tyrosine")
        if "UAC" in single_strand:
            prot.append("Tyrosine")
        if "UGU" in single_strand:
            prot.append("Cysteine")
        if "UGC" in single_strand:
            prot.append("Cysteine")
        if "UGG" in single_strand:
            prot.append("Tryptophan")
        if "UAA" in single_strand:
            break
        if "UAG" in single_strand:
            break
        if "UGA" in single_strand:
            break
    return prot





print(proteins("AUG"))
# expected = ["Methionine"]

print(proteins("UUU"))
# expected = ["Phenylalanine"]

print(proteins("UUC"))
# expected = ["Phenylalanine"]

print(proteins("UUA"))
# expected = ["Leucine"]

print(proteins("UUG"))
# expected = ["Leucine"]

print(proteins("UCU"))
# expected = ["Serine"]

print(proteins("UCC"))
# expected = ["Serine"]

print(proteins("UCA"))
# expected = ["Serine"]

print(proteins("UCG"))
# expected = ["Serine"]

print(proteins("UAU"))
# expected = ["Tyrosine"]

print(proteins("UAC"))
# expected = ["Tyrosine"]

print(proteins("UGU"))
# expected = ["Cysteine"]

print(proteins("UGC"))
# expected = ["Cysteine"]

print(proteins("UGG"))
# expected = ["Tryptophan"]

print(proteins("UAA"))
# expected = []

print(proteins("UAG"))
# expected = []

print(proteins("UGA"))
# expected = []

print(proteins("UUUUUU"))
# expected = ["Phenylalanine", "Phenylalanine"]

print(proteins("UUAUUG"))
# expected = ["Leucine", "Leucine"]

print(proteins("AUGUUUUGG"))
# expected = ["Methionine", "Phenylalanine", "Tryptophan"]

print(proteins("UAGUGG"))
# expected = []

print(proteins("UGGUAG"))
# expected = ["Tryptophan"]

print(proteins("AUGUUUUAA"))
# expected = ["Methionine", "Phenylalanine"]

print(proteins("UGGUAGUGG"))
# expected = ["Tryptophan"]

print(proteins("UGGUGUUAUUAAUGGUUU"))
# expected = ["Tryptophan", "Cysteine", "Tyrosine"]
