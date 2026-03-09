# 소수 구하기

# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

import sys
input = sys.stdin.readline

M, N = map(int, input().split())

prime = [True] * (N + 1)
prime[0] = prime[1] = False

for i in range(2, int(N ** 0.5) + 1):
    if prime[i]:
        # range(시작, 끝, 간격)
        for j in range(i * i, N + 1, i):
            prime[j] = False
            
for i in range(M, N + 1):
    if prime[i]:
        print(i)