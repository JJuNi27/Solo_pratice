# '구분자'.join(리스트)
# 리스트의 요소들을 '구분자'로 이어붙인 하나의 문자열로 만들어줌
# 예시
list_example = ['Hello', 'World', 'Python']
result = ' '.join(list_example)
print(result)  
# 내부적으로 'Hello' + ' ' + 'World' + ' ' + 'Python'
# 출력: Hello World Python

lst = ['A', 'B', 'C']
print(''.join(lst))
# 출력: ABC

print('-'.join(lst))
# 출력: A-B-C

# 중간에 문자열 말고 숫자가 들어있는 경우에는 오류가 발생함
# lst2 = ['A', 1, 'C']
# print('-'.join(lst2))
# TypeError: sequence item 1: expected str instance, int found

# 나 혼자 테스트

list_good = ['gojo', 'satoru']
print('_'.join(list_good))