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
