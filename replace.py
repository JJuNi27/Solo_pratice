# 문자열.replace(기존문자열, 새문자열)
# 문자열에서 기존문자열을 찾아서 전부 새문자열로 바꾼 결과를 반환
text = "Hello, World!"
new_text = text.replace("World", "Python")
print(new_text)  # "Hello, Python!"
print(text)      # "Hello, World!" (원본 문자열은 변경되지 않음)