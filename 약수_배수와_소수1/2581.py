# 소수

# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

# 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
# M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 
# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.


# 정답은 맞지만 시간초과로 실패 코드를 더 압축해야함!!!!!
# M = int(input())
# N = int(input())

# # M 이상 N 이하의 자연수를 먼저 찾아보자
# # nat은 M과 N 사이의 자연수 리스트
# nat = list(range(M, N + 1))

# # 리스트 확인용
# print(nat)

# # 소수 전용 리스트
# result = []

# for num in nat:
#     # 약수 리스트
#     divs = []
#     # 리스트에 담긴 숫자 하나씩 약수 검사 시작
#     for i in range(1, num + 1):
#         # 약수이면 약수 리스트에 몫 추가
#         if num % i == 0:
#             divs.append(i)
#     # 약수의 몫이 2개뿐이면 소수 리스트에 해당 숫자 추가        
#     if len(divs) == 2:
#         result.append(num)

# # result(소수)의 값이 존재한다면
# if (len(result)) >= 1:
#     # 리스트의 핪
#     print(sum(result))
#     # 리스트의 최솟값
#     print(min(result))
# # result(소수)의 값이 존재하지 않는다면
# else:
#     # 없으면 -1
#     print(-1)

# ----------------------------

M = int(input())
N = int(input())

# M 이상 N 이하의 자연수를 먼저 찾아보자
# nat은 M과 N 사이의 자연수 리스트
nat = list(range(M, N + 1))

# 소수 전용 리스트
result = []

for num in nat:
    if num < 2:
        continue
    # 플래그(처음엔 소수라고 가정)
    is_prime = True
    # 리스트에 담긴 숫자 하나씩 약수 검사 시작
    for i in range(2, int(num**0.5) + 1):
        # 약수가 아니라면 소수가 아니다라고 판정 후 break
        if num % i == 0:
            is_prime = False
            break
    # 약수의 몫이 2개뿐이면 소수 리스트에 해당 숫자 추가        
    if is_prime:
        result.append(num)

# result(소수)의 값이 존재한다면
if (len(result)) >= 1:
    # 리스트의 핪
    print(sum(result))
    # 리스트의 최솟값
    print(min(result))
# result(소수)의 값이 존재하지 않는다면
else:
    # 없으면 -1
    print(-1)