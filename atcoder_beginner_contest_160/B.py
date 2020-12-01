import math

X = int(input())
total_500 = 0
total_5 = 0
total_count = 0

if(X >= 500):
    total_500 = math.floor(X/500)
    total_count += total_500 * 1000
    X -= total_500 * 500

if(X >= 5):
    total_5 = math.floor(X/5)
    total_count += total_5 * 5
    X -= total_5 * 5

print(total_count)
