# from collections import deque
# queue = deque()
# queue.append(x)   # 넣기
# queue.popleft()   # 앞에서 빼기
# queue[0]          # 맨 앞
# queue[-1]         # 맨 뒤
# len(queue)        # 크기
# if queue:         # 안 비었으면 True

# ==============================
# 큐(Queue) 핵심 문법 정리
# ==============================

# 큐는 "먼저 들어간 게 먼저 나오는 구조"
# 예: 1 넣고, 2 넣고, 3 넣으면 -> 뺄 때 1부터 나옴
# 영어로는 FIFO (First In First Out)

# 큐는 보통 list 말고 deque를 사용
# 이유: 맨 앞 삭제가 빠름
from collections import deque

# 큐 생성
queue = deque()

# 1. push : 값 넣기
# 의미: 큐 맨 뒤에 값 추가
# 사용법: queue.append(값)
queue.append(10)
queue.append(20)

# 2. pop : 값 꺼내기
# 의미: 큐 맨 앞 값을 꺼내고 삭제
# 사용법: queue.popleft()
# 주의: 비어있는데 popleft() 하면 에러남
if queue:
    x = queue.popleft()

# 3. front : 맨 앞 값 확인
# 의미: 큐 맨 앞 값만 보기 (삭제는 안 함)
# 사용법: queue[0]
if queue:
    x = queue[0]

# 4. back : 맨 뒤 값 확인
# 의미: 큐 맨 뒤 값만 보기 (삭제는 안 함)
# 사용법: queue[-1]
if queue:
    x = queue[-1]

# 5. size : 큐 크기
# 의미: 큐 안에 들어있는 원소 개수
# 사용법: len(queue)
print(len(queue))

# 6. empty : 비어있는지 확인
# 의미: 비어있으면 False, 값 있으면 True
# 사용법: if queue:
if queue:
    print("안 비어있음")
else:
    print("비어있음")

# 백준식 empty 출력 예시
# 비어있으면 1, 아니면 0
print(0 if queue else 1)


# ==============================
# 스택 / 큐 차이 한 줄 정리
# ==============================

# 스택
# 넣기: append()
# 빼기: pop()
# 맨 위 확인: [-1]

# 큐
# 넣기: append()
# 빼기: popleft()
# 맨 앞 확인: [0]
# 맨 뒤 확인: [-1]