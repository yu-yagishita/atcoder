def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

N, K = [int(_) for _ in input().split()]

print(Base_10_to_n(N, K))

print(len(Base_10_to_n(N, K)))
