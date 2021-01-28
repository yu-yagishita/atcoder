X, Y = map(int, input().split())
losser = 0
winner = 0
if X > Y:
    losser = Y
    winner = X
else:
    losser = X
    winner = Y

if losser+3 > winner:
    print('Yes')
else:
    print('No')
