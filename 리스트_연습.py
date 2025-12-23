list_good = [0,1,2,3,4,5,6]

print("리스트 :", list_good)

max_value = max(list_good)
# 최대값 인덱스 위치
max_index = list_good.index(max_value)
print("최대값 :", max_value)
# 최대값 순서
max_index = list_good.index(max_value) + 1
print("최대값 위치 :", max_index)

# ---------------------------------------------------

# 두 수의 합 구하기
# 숫자용
sum_value = 0

# 문자용
sum_str = ""

for i in range(2):
    row = list(input().split())
    # sum_value += int(row[i])
    sum_str += row[i]
print(row)
# print(sum_value)
print(sum_str)