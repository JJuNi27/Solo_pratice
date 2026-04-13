# 리스트.sort()
# 👉 리스트 안의 요소들을 “오름차순”으로 직접 정렬한다

# 오름차순
lst = [3, 1, 4, 2]
lst.sort()
print(lst)

# 출력
[1, 2, 3, 4]

# 내림차순
lst.sort(reverse=True)

lst = [1, 4, 2]
lst.sort(reverse=True)
print(lst)

# 출력
[4, 2, 1]

# sorted() : “정렬된 새 리스트”를 만들어서 반환

# 원본은 안 바뀜

# 리스트 말고도(튜플, 문자열 등) **반복 가능한 것(iterable)**이면 대부분 됨

nums = [3, 1, 2]
new_nums = sorted(nums)

print(nums)      # [3, 1, 2]  (원본 그대로)
print(new_nums)  # [1, 2, 3]  (새로 만들어짐)