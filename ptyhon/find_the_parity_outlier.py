def find_outlier(integers):
    print(integers)
    odd = 0
    even = 0
    o = False
    e = False
    c = 0
    prev = 0
    for i in integers:
        if not i % 2:
            even = i
            e = True
        else:
            o = True
            odd = i
        if c > 1 and o and e:
            if c == 2 and ((i % 2) == (integers[0] % 2)):
                print("entrou")
                if even == prev:
                    return even
                else:
                    return odd
            if prev % 2 == odd % 2:
                return even
            else:
                return odd
        prev = i
        c += 1
    return integers[0]
