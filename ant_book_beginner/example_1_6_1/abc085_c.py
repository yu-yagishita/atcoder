n, Y = map(int, input().split())
Y //= 1000
for x in range(n+1):
   for y in range(n+1):
       z = n-x-y
       if z < 0:
           continue
       if 10*x+5*y+z==Y:
           print(x, y, z)
           exit(0)
print(-1, -1, -1)
