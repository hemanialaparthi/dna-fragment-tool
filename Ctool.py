# Coltins take

def align_sequences(sequences):
    """Aligns a list of sequences and prints them with mismatches highlighted."""
    ref = sequences[0]      # Use first sequence as reference
    aligned = [list(ref)]   # Start aligned list with reference sequence

    for seq in sequences[1:]:
        aligned_seq = []
        # compare each character in the reference to the current sequence
        for r, s in zip(ref, seq.ljust(len(ref))):      # add spaces to shorter seq
            if r == s:
                aligned_seq.append(s)    # match keep character
            else:
                aligned_seq.append(" ")  # mismatch insert space
        aligned.append(aligned_seq)      # add aligned sequence to list

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
