# 좌표 압축

# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

# 첫째 줄에 N이 주어진다.
# 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

# 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

import sys
input = sys.stdin.readline

N = int(input())
    
lit = list(map(int, input().split()))

# lit = [2, 4, -10, 4, -9]

lit_sort = sorted(set(lit))

# lit_sort = [-10, -9, 2, 4]

rank = {}
for i, v in enumerate(lit_sort):
    rank[v] = i

# rank  
# {
#   -10: 0,
#   -9: 1,
#   2: 2,
#   4: 3
# }

ans = []
for x in lit:
    ans.append(rank[x])
    
# lit가 [2, 4, -10, 4, -9]라면

# rank[x]는 [2, 3, 0, 3, 1]이 됨.

print(*ans)

# 고수용
# rank = {v: i for i, v in enumerate(lit_sort)}  # 값 -> 순위

# print(*[rank[x] for x in lit])