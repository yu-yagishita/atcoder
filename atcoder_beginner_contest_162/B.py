N = int(input())

ans = []
ans_num = 0
for i in range(N):
    s = i+1
    if(s%3 == 0 and s%5 == 0):
        ans.append("FizzBuzz")
    elif(s%3 == 0):
        ans.append("Buzz")
    elif(s%5 == 0):
        ans.append("Buzz")
    else:
        ans.append(s) 
        ans_num += s

print(ans_num)
