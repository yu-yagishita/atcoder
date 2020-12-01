N=int(input())
count=0
T,X,Y=0,0,0
for i in range(N):
    t,x,y = [int(_) for _ in input().split()]
    if abs(x-X)+abs(y-Y)<=t-T and t%2==(x+y)%2:
        count+=1
    T,X,Y=t,x,y
print("Yes" if count==N else "No")
