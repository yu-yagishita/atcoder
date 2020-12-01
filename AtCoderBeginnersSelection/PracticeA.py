from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

a = int(input())
b, c = [int(_) for _ in input().split()]
d  = input()
print(str(a + b + c) + ' ' + d)
