# 알파벳 찾기

# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않는다. 단어는 알파벳 소문자로만 이루어져 있다.

S = input()

baekjoon = 'abcdefghijklmnopqrstuvwxyz'

for i in baekjoon:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')