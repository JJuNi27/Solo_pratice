# 수 정렬하기 3

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

import sys
input = sys.stdin.readline

N = int(input())
count = [0] * 10001

for _ in range(N):
    count[int(input())] += 1

write = sys.stdout.write

CHUNK = 1000  # 한 번에 최대 1000줄씩만 만들어서 출력 (메모리 폭발 방지)

for i in range(1, 10001):
    c = count[i]
    if c:
        line = f"{i}\n"
        while c > 0:
            k = CHUNK if c > CHUNK else c
            write(line * k)
            c -= k
