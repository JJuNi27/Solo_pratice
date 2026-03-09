# 다음 소수

# 정수 n(0 ≤ n ≤ 4*109)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.

# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.

# 각각의 테스트 케이스에 대해서 n보다 크거나 같은 소수 중 가장 작은 소수를 한 줄에 하나씩 출력한다.

import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    val = int(input())

    # 무한반복 소수 입력
    while True:
        # val이 소수인지 판단
        is_prime = True
        # 2보다 작으면 소수가 아니다
        if val < 2:
            is_prime = False
        else:
            # 소수 찾기
            for i in range(2, int(val**0.5) + 1):
                if val % i == 0:
                    is_prime = False
                    break
        # 소수라면 출력
        if is_prime:
            print(val)
            break
        # 소수가 아니라면 +1씩 해서 소수찾기
        else:
            val += 1
