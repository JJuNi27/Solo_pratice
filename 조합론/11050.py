# 이항 계수

# 자연수 N과 정수 K가 주어졌을 때 이항 계수 \binom{N}{K}를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 0 ≤ K ≤ N)

# 출력
 
# \binom{N}{K}를 출력한다.

import math
import sys
input = sys.stdin.readline

N,K = map(int,input().split())

N_f = math.factorial(N)
K_f = math.factorial(K)
cross_f = math.factorial(N-K)

print(int(N_f / (K_f * cross_f)))

# 숏코딩 버전--------------------

# import math

# N, K = map(int, input().split())
# print(math.comb(N, K))