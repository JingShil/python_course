import math

def nearest_sq(n):
    sqrt_n = int(math.sqrt(n))  
    if sqrt_n * sqrt_n == n: 
        return n
    else:
        lower_sq = sqrt_n * sqrt_n  
        upper_sq = (sqrt_n + 1) * (sqrt_n + 1)  
        if n - lower_sq < upper_sq - n:  
            return lower_sq
        else:
            return upper_sq