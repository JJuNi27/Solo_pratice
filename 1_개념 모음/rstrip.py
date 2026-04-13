import sys

input = sys.stdin.readline

# rstrip()쓰면 뒤에 안보이는 줄바꿈 \n이 사라짐(글자수 정상화)
print("지금 쓰는 단어 수에 +1일거야 rstrip을 안썼거든")
N = input()

print(len(N))

print("같은 단어 한번 더 써봐 이번엔 정상화 되어있을거야")
S = input().rstrip()

print(len(S))