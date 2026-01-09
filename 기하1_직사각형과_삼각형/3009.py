# 네 번째 점

# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

# 직사각형의 네 번째 점의 좌표를 출력한다.

# x,y 각각 좌표의 카운트 수가 더 적을걸 출력하면 될 듯 하오

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x_list = [x1,x2,x3]
y_list = [y1,y2,y3]

freq_x = {}

for x in x_list:
    freq_x[x] = freq_x.get(x, 0) + 1

# 입력 예시
# 5 5
# 5 7
# 7 5
# freq_x = {5:2, 7:1}
    
freq_y = {}
for y in y_list:
    freq_y[y] = freq_y.get(y, 0) + 1

for x in freq_x:
    if freq_x[x] == 1:
        x4 = x
        
for y in freq_y:
    if freq_y[y] == 1:
        y4 = y

print(x4,y4)

# -------------(챗봇 정답)

# x = 0
# y = 0

# for _ in range(3):
#     a, b = map(int, input().split())
#     x ^= a
#     y ^= b

# print(x, y)

# XOR의 특징 중
# 자기 자신과 XOR이 되면 지워지는 특징을 이용
# 입력 예시(5, 5, 7)
# x = 0
# x ^= 5   # 0 ^ 5 = 5
# x ^= 5   # 5 ^ 5 = 0
# x ^= 7   # 0 ^ 7 = 7
