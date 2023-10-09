def bouncingBall(h, bounce, window):
    if not 0 < bounce < 1: return -1
    if not 0 < window < h: return -1
    count = 1
    while h * bounce > window:
        h *= bounce
        count += 2
    return count
