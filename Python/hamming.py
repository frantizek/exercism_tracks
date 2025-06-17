def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        return len([a+b for a, b in zip(strand_a, strand_b) if a != b])
    else:
        # When the sequences being passed are not the same length.
        raise ValueError("Strands must be of equal length.")
