# **enumerate(리스트)**는 “인덱스랑 값을 같이” 꺼내주는 도구야.

lit_sort = [-10, -9, 2, 4]

for i, v in enumerate(lit_sort):
    print(i, v)

# 출력
# 0 -10
# 1 -9
# 2 2
# 3 4

# 즉,
# i는 인덱스(0,1,2,3…)
# v는 실제 값(-10,-9,2,4…)