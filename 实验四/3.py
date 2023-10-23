def protein(rna):
    protein_sequence = ''
    codon = ''

    for letter in rna:
        codon += letter
        if len(codon) == 3:
            if PROTEIN_DICT[codon] == 'Stop':
                break
            protein_sequence += PROTEIN_DICT[codon]
            codon = ''

    return protein_sequence