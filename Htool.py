def align_dna_sequences(sequences):
    """
    Simple DNA sequence alignment function.
    Takes a list of DNA sequences and returns them aligned.
    """

    if len(sequences) < 2:
        return sequences

    # start with the first sequence
    aligned = [sequences[0]]

    # add each other sequence one by one
    for new_seq in sequences[1:]:
        best_alignment = None
        best_score = -999

        # try placing the new sequence at different positions
        for offset in range(-len(new_seq), len(aligned[0]) + 1):
            # Create test alignment
            test_aligned = []

            # copy existing sequences
            for seq in aligned:
                if offset < 0:
                    # need to add gaps to the left of existing sequences
                    test_aligned.append('-' * abs(offset) + seq)
                else:
                    test_aligned.append(seq)

            # add new sequence with gaps
            if offset >= 0:
                new_with_gaps = '-' * offset + new_seq
            else:
                new_with_gaps = new_seq

            # make all sequences the same length
            max_len = max(len(s) for s in test_aligned + [new_with_gaps])
            test_aligned = [s + '-' * (max_len - len(s)) for s in test_aligned]
            new_with_gaps = new_with_gaps + '-' * (max_len - len(new_with_gaps))
            test_aligned.append(new_with_gaps)

            # score this alignment (count matches)
            score = 0
            for pos in range(max_len):
                column = [seq[pos] for seq in test_aligned]
                # count how many characters match the most common one
                for char in 'ACGT':
                    count = column.count(char)
                    if count > 1:
                        score += count * 2  # bonus for matches

                score -= column.count('-')  # penalty for gaps

            # keep track of best alignment
            if score > best_score:
                best_score = score
                best_alignment = test_aligned

        aligned = best_alignment

    return aligned


if __name__ == "__main__":
    # example DNA sequences
    sequences = [
        "ACGTGCA",
        "CGTGC",
        "GTGCA",
        "TGCAT"
    ]
    aligned = align_dna_sequences(sequences)
    print("Aligned DNA Sequences:")
    for seq in aligned:
        print(seq)
