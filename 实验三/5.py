def disemvowel(string):
    vowels = 'aeiouAEIOU'
    return ''.join(c for c in string if c not in vowels)