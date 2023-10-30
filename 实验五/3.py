def is_pangram(sentence):
    # 将字符串转换为小写，并去除数字和标点符号
    sentence = ''.join(c.lower() for c in sentence if c.isalpha())
    # 使用set()函数获取唯一字母集合，并检查数量是否等于26
    return len(set(sentence)) == 26