# Coltins take

def align_sequences(sequences):
    """Aligns a list of sequences and prints them with mismatches highlighted."""
    ref = sequences[0]
    aligned = [list(ref)]

    for seq in sequences[1:]:
        aligned_seq = []
        for r, s in zip(ref, seq.ljust(len(ref))):  # pad shorter seq
            if r == s:
                aligned_seq.append(s)
            else:
                aligned_seq.append(" ")
        aligned.append(aligned_seq)

    # Print results
    for seq in aligned:
        print("".join(seq))


if __name__ == "__main__":
    sequences = [
        "caggatta",
        "cagggata",
        "cgcctatt",
        "cagaatta"
    ]
    align_sequences(sequences)
