N = int(input())

# range는 0부터 N-1까지의 숫자를 생성하는 함수 (문자열은 range에 못 넣음)
print(range(N))

# range 객체를 리스트로 변환하여 출력
print(list(range(N)))

S = input()

# range(S)와 S의 차이
# for i in range(S):
#     print(i)
# -> S는 문자열 이기에 오류 발생

for i in range(5):
    print(i)
# -> 0 1 2 3 4 출력

for i in S:
    print(i)
# -> S의 각 문자 출력