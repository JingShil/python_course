def spinWords(words):
    word_list = words.split()
    for i in range(len(word_list)):
        if len(word_list[i]) >= 5:
            word_list[i] = word_list[i][::-1]
    return ' '.join(word_list)