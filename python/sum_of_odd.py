def row_sum_odd_numbers(n):
    return sum(map(lambda x: x*2 -1, (range(((n*(n+1))//2) - n + 1, (n*(n+1)//2)+1))))
