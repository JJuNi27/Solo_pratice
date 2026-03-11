# 베르트랑 공준

# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.
# 입력의 마지막에는 0이 주어진다.

# 각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

# 어떻게 해볼까
# 일단 무한 반복하고 입력이 0이면 종료
# n부터 n+1까지 반복하며 소수를 카운트하자 그리고 출력하는거야

import sys
input = sys.stdin.readline

nums = []

while True:
    n = int(input())
    if n == 0:
        break
    nums.append(n)

limit = 2 * max(nums)
prime = [True] * (limit + 1)
prime[0] = prime[1] = False

for i in range(2, int(limit ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, limit + 1, i):
            prime[j] = False

for n in nums:
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if prime[i]:
            count += 1
    print(count)


# 내가 쓴 코드
# -------------------------------------

# while True:
#     val = int(input())
#     # 소수를 세는 카운트
#     count = 0
#     # 0이면 종료
#     if val == 0:
#         break
#     else:
#         # n부터 2n까지
#         for i in range(val + 1,(2*val) + 1):
#             # 소수인지 판별
#             is_prime = True
#             # 소수 판별
#             if i < 2:
#                 is_prime = False
#             else:
#                 for j in range(2, int(i**0.5) + 1):
#                     if i % j == 0:
#                         is_prime = False
#                         break
#                 if is_prime:
#                     count += 1
#     print(count)