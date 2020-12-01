N = int(input())
A = [int(_) for _ in input().split()]
alice = 0
bob = 0
alice_count = 0
bob_count = 0
while N!=(alice_count + bob_count):
    max = 0
    for i in A:
        if max < i:
            max = i
    if alice_count <= bob_count:
        alice += max
        alice_count += 1
    else:
        bob += max
        bob_count += 1
    A.remove(max)
print(alice - bob)
