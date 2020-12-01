a = int(input())
b = int(input())
c = int(input())
X = int(input())
count = 0
for i in range(a+1):
    for v in range(b+1):
        for z in range(c+1):
            total = (i)*500 + (v)*100 + (z)*50
            if total == X:
                count += 1
print(str(count))
