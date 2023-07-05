def compute_stats(data):
    n = 0
    sum = 0.0
    sum2 = 0.0
    for value in data:
        n += 1
        sum += value
    mean = sum/n
    for value in data:
        sum2 += (value - mean)**2
    stddev = sqrt(sum2/(n - 1))
    return n, mean, stddev
