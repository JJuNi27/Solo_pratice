a = [1,2]      # list
b = (1,2)      # tuple
c = {1,2}      # set
d = {"a": 1}   # dict
e = {}         # dict (빈 dict)
f = set()      # set (빈 set)

# 추가(넣기) 메서드 정리
# ✅ set
# add(x) : 원소 1개 추가
# update(iterable) : 여러 개 추가(리스트/세트 등 한꺼번에)

# ✅ list
# append(x) : 원소 1개 추가
# extend(iterable) : 여러 개 “펼쳐서” 추가

# ✅ dict (너가 물어본 거!)
# 딕셔너리는 “키:값” 구조라서 보통 이렇게 넣어:
# d = {}
# d["apple"] = 3   # 추가/수정 (가장 흔함)

# 여러 개를 한꺼번에 합치려면:
# d.update({"banana": 2, "cat": 5})

c = {1, 2}        # 콜론(:) 없음 → set
d = {"a": 1}      # 콜론(:) 있음 → dict
e = {}            # 비어있음 → dict (빈 set로 해석 불가)
f = set()         # 빈 set는 이렇게만 만들 수 있음
