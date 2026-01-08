# 직사각형에서 탈출

# 한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

# 첫째 줄에 x, y, w, h가 주어진다.

# 첫째 줄에 문제의 정답을 출력한다.

# 그니까 내가 (x,y)에 있고 (0,0),(w,h)인 직사각형이 있는데?
# 내가 이 직사각형에서 가장 가까운 경계선(변)까지 가는 거리를 구하라..

x, y, w, h = map(int, input().split())

left = abs(0 - x)
right = w - x
up = h - y
down = abs(0 - y)

result = [left, right, up, down]

print(min(result))

# -------------------(챗봇 정답)

# x, y, w, h = map(int, input().split())
# print(min(x, w - x, y, h - y))
