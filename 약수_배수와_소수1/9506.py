# 약수들의 합

# 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.

# 예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.

# n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.

# 입력은 테스트 케이스마다 한 줄 간격으로 n이 주어진다. (2 < n < 100,000)

# 입력의 마지막엔 -1이 주어진다.

# 테스트케이스 마다 한줄에 하나씩 출력해야 한다.

# n이 완전수라면, n을 n이 아닌 약수들의 합으로 나타내어 출력한다(예제 출력 참고).

# 이때, 약수들은 오름차순으로 나열해야 한다.

# n이 완전수가 아니라면 n is NOT perfect. 를 출력한다.

while True:
    n = int(input())
    
    # n의 약수 리스트
    list_n = []
    # n의 약수를 전부 합하는 변수명
    every = 0

    # -1 누르면 종료    
    if n == -1:
        break
    
    # n의 약수인지 판별, 약수라면 list_n에 몫 추가
    for i in range(1, n+1):
        if n % i == 0:
            # 이 때 n의 값이랑 같은 몫은 제외
            if n != i:
                list_n.append(i)
    
    # list_n의 몫들을 전부 더하여 every에 값 저장
    every = sum(list_n)

    # n이랑 약수의 몫들을 합한 값(every)이 같으면 문제가 원하는 문장 출력
    if n == every:
        # n = 6이라고 했을 때 [1,2,3]을 1+2+3으로 바꿔줌
        print(str(n) + " = " + " + ".join(map(str,list_n)))
    # 같지 않다면 완벽하지 않다고 출력
    else:
        print(str(n) + " is NOT perfect.")
    
    # 디버깅용
    # print(list_n)
    # print(every)
    # print(perfect_list)
    
    # ---------
    
    # 챗봇이 말한 정답    
    # while True:
    # n = int(input())
    # if n == -1:
    #     break

    # divs = [1]
    
    # for i in range(2, int(n**0.5) + 1):
    #     if n % i == 0:
    #         divs.append(i)
    #         if i != n // i:
    #             divs.append(n // i)

    # divs.sort()
    # div_sum = sum(divs)

    # if div_sum == n:
    #     print(f"{n} = " + " + ".join(map(str, divs)))
    # else:
    #     print(f"{n} is NOT perfect.")
