A, B, C = map(int, input().split())

if C == 0:
    while True:
        if A>0:
            A -= 1
        else:
            print('Aoki')
            exit(0)
        if B>0:
            B -= 1
        else:
            print('Takahashi')
            exit(0)
else:
    while True:
        if B>0:
            B -= 1
        else:
            print('Takahashi')
            exit(0)
        if A>0:
            A -= 1
        else:
            print('Aoki')
            exit(0)
