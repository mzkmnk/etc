import sys, re
#------pypyで再帰などを提出する場合は下記２行を使用-----
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')
# import numpy as np
from math import ceil, floor, sqrt, pi, factorial, gcd,isfinite
from copy import deepcopy
from collections import Counter, deque,defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement,permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce,lru_cache
#メモ化の場合は下記を使用
#@lru_cache(maxsize=1000)
from decimal import Decimal, getcontext
# input = sys.stdin.readline 
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_none_map(): return map(int,input())
def i_list(): return list(i_map())
def i_none_list(): return list(i_none_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

#7 <= N <= 10**5
#0 -> 休日 1->平日
#O(N)
#休日：holiday
#平日：weekday
N = i_input()
d = i_list()
holiday,weekday,result,cnt = 0,0,0,0
deq = deque()

for n in range(7):
    cnt += 1
    if d[n] == 0: holiday += 1
    else: weekday += 1
    deq.append(d[n])
if holiday < 2: cnt = 0
for n in range(7,N):
    # print(deq,cnt,result)
    if d[n] == 0: holiday += 1
    else: weekday += 1
    deq.append(d[n])
    del_day = deq.popleft()
    if del_day == 0: holiday -= 1
    else: weekday -= 1
    # print(holiday,weekday)
    if holiday < 2: 
        result = max(result,cnt)
        cnt = 0
    else:
        if cnt == 0: cnt = 7
        else:cnt += 1
print(max(result,cnt))