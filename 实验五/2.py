def find_outlier(arr):
    odd_count = 0
    even_count = 0
    odd_num = 0
    even_num = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
            even_num = num
        else:
            odd_count += 1
            odd_num = num
    if odd_count > 1:
        return even_num
    else:
        return odd_num