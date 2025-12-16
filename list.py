N = int(input())

list_extend = []
list_append = []

for i in range(N):
    S = input()
    
    # +=는 extend와 동일하게 작동. 만약에 'hi'를 추가한다면 list.extend('hi') => 'h', 'i'가 추가됨
    list_extend += S


    # append는 리스트에 요소를 추가함 만약에 'hi'를 추가한다면 list.append('hi') => 'hi'가 추가됨
    list_append.append(S)

print("+=(extend)의 결과" + str(list_extend))
print("append의 결과" + str(list_append))

# extend = 확장하다
# append = 덧붙이다