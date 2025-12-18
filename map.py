a, b = map(int, input().split())

# a, b = int(input().split()) <- 이건 안됨

# split()은 문자열을 나누어 리스트로 만들어주는 함수이기 때문에
# input()으로 들어오는 값은 문자열이므로
# int()로 바로 변환할 수 없음(list는 int()로 변환 불가)

# int()는 문자열 하나만 변환 가능

# map의 역할
# 리스트 안의 모든 요소에 대해 각각 int()를 적용시켜줌
# 결과적으로 a와 b는 각각 정수형으로 변환되어 저장됨

# 응용

nums = list(map(int, input().split()))
print(nums)  # 입력된 숫자들이 정수형 리스트로 저장됨