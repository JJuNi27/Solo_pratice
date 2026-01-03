# 약수 구하기

# 어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다. 

# 6을 예로 들면

# 6 ÷ 1 = 6 … 0
# 6 ÷ 2 = 3 … 0
# 6 ÷ 3 = 2 … 0
# 6 ÷ 4 = 1 … 2
# 6 ÷ 5 = 1 … 1
# 6 ÷ 6 = 1 … 0
# 그래서 6의 약수는 1, 2, 3, 6, 총 네 개이다.

# 두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다. N은 1 이상 10,000 이하이다. K는 1 이상 N 이하이다.

# 첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력하시오.

N, K = map(int, input().split())

# 약수 갯수용 리스트
list_N = []
# 약수의 몫용 리스트
list_sq = []

for i in range(N):
    # 몫 확인용
    sq = i + 1
    
    # N값의 약수 확인해보기
    result = N % (i + 1)
    # N값의 몫 확인해보기
    sq_result = N // (i + 1)
    # # 디버깅용
    # print(i+1 , "번째의 나머지 값" , result)
    # print(i+1 , "번째의 몫 값" , result)
    
    # 약수만 리스트에 넣기
    if result == 0:
        list_N.append(result)
        list_sq.append(sq_result)
    
    # # 디버깅용
    # print(list_N)
    # print(list_sq)

# 리스트 순서 뒤집기
final_list = list_sq[::-1]
# # 디버깅용
# print(final_list)

if len(list_N) < K:
    print(0)
else:
    print(final_list[K-1])


# 챗봇이 말한 정답
# N, K = map(int, input().split())

# divs = []
# for i in range(1, N+1):
#     if N % i == 0:
#         divs.append(i)

# if len(divs) < K:
#     print(0)
# else:
#     print(divs[K-1])
