# split()이란?

# 문자열을 기준 문자로 나누어서 리스트(list)로 만들어주는 함수

# 문자열.split(기준)


s = "apple,banana,orange"
print(s.split(","))
# 출력: ['apple', 'banana', 'orange']

# , 을 기준으로 문자열을 나누어서 리스트로 만들어줌
# "" 사용 이유는 문자열임을 명시하기 위해서




# 입력 예시

# 734 893

a = input()
print(a)

# 결과
# "734 893"

# 2908.py와 비교

# a,b = input()

# input()  →  "734 893"

# a = '7'
# b = '3'

# a, b = input().split()

# a = '734'
# b = '893'