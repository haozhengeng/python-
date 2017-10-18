def flatten(nested):
    try:
        if isinstance(nested, str):
            raise TypeError
        for sublist in nested:   # int字节在for中遍历的时候也会报TypeError
            for element in flatten(sublist):
                # print("got", element, end=";")
                  yield element
    except TypeError:
        yield nested

L = ["aaaa", [1, 2, 3], 2, 4, [5, [6, [8, [9]], "adf"], 7]]
for num in flatten(L):
    print(“--”)   # 利用for循环只是为了迭代生成器 
# >>> got aaaa;got 1;got 2;got 3;got 2;got 4;got 5;got 6;got 8;got 9;got adf;got 7;
