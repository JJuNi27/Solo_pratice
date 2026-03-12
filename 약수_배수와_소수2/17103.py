# 골드바흐 파티션

# 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
# 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.

# 첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 100)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 N은 짝수이고, 2 < N ≤ 1,000,000을 만족한다.

# 각각의 테스트 케이스마다 골드바흐 파티션의 수를 출력한다.

import sys

input = sys.stdin.readline

T = int(input())

num = [int(input()) for _ in range(T)]

max_n = max(num)
prime = [True] * (max_n + 1)
prime[0] = prime[1] = False

for i in range(2, int(max_n**0.5) + 1):
    if prime[i]:
        for j in range(i * i, max_n + 1, i):
            prime[j] = False
            
for n in num:
    count = 0
    for i in range(2, n // 2 + 1):
        if prime[i] and prime[n-i]:
            count += 1
    print(count)


# 6 = 3+3
# 8 = 1+7, 3+5
