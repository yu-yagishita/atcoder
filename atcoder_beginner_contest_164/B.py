N = [int(_) for _ in input().split()]
A = N[0]
B = N[1]
C = N[2]
D = N[3]

while True:
    C -= B
    if A<= 0:
        print("No")
        break
    A -= D
    if C<= 0:
        print("Yes")
        break
