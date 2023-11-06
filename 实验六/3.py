def shorten_number(suffixes, base):
    def filter_func(num):
        if isinstance(num, str) and num.isdigit():
            num = int(num)
            for i, suffix in enumerate(suffixes):
                if num < base ** (i+1):
                    return str(num // base ** i) + suffix
            return str(num // base ** (len(suffixes)-1)) + suffixes[-1]
        return str(num)
    return filter_func