# stack = []
# stack.append(x)   # 넣기
# stack.pop()       # 빼기
# stack[-1]         # 맨 위
# len(stack)        # 크기
# if stack:         # 안 비었으면 True

# ==============================
# 스택(Stack) 핵심 문법 정리
# ==============================

# 스택은 "나중에 들어간 게 먼저 나오는 구조"
# 예: 1 넣고, 2 넣고, 3 넣으면 -> 뺄 때 3부터 나옴
# 영어로는 LIFO (Last In First Out)

# 스택 생성
stack = []

# 1. push : 값 넣기
# 의미: 스택 맨 위에 값 추가
# 사용법: stack.append(값)
stack.append(10)
stack.append(20)

# 2. pop : 값 꺼내기
# 의미: 스택 맨 위 값을 꺼내고 삭제
# 사용법: stack.pop()
# 주의: 비어있는데 pop() 하면 에러남
if stack:
    x = stack.pop()

# 3. top : 맨 위 값 확인
# 의미: 스택 맨 위 값만 보기 (삭제는 안 함)
# 사용법: stack[-1]
# 주의: 비어있는데 stack[-1] 하면 에러남
if stack:
    x = stack[-1]

# 4. size : 스택 크기
# 의미: 스택 안에 들어있는 원소 개수
# 사용법: len(stack)
print(len(stack))

# 5. empty : 비어있는지 확인
# 의미: 비어있으면 True처럼 취급 안 됨 / 값 있으면 True
# 사용법: if stack:
if stack:
    print("안 비어있음")
else:
    print("비어있음")

# 백준식 empty 출력 예시
# 비어있으면 1, 아니면 0
print(0 if stack else 1)