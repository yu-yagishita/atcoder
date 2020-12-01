A1, A2, A3 = [int(_) for _ in input().split()]
if A1+A2+A3 >= 22:
    print("bust")
if A1+A2+A3 <= 21:
    print("win")
