def recoverSecret(triplets):
    chars = set([c for triplet in triplets for c in triplet])
    sorted_chars = []
    while chars:
        for c in chars:
            if all(c not in triplet[1:] for triplet in triplets):
                chars.remove(c)
                sorted_chars.append(c)
                for triplet in triplets:
                    if triplet and triplet[0] == c:
                        triplet.pop(0)
                break
    return ''.join(sorted_chars)