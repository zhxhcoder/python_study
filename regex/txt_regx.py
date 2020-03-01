import re

regex = re.compile(r'\b\w{6}\b')  # 匹配6个字符的单词
text = regex.search('My number is greats ')
text.group()  # 调用 group() 返回结果

print(text.group())

m = re.match(r"(\w+)\s+(\w+)", "Isaac Newton, physicist")
print(m.group())
print(m.group(0))  # The entire match
print(m.group(2))
print(m.group(3))
print(m.group(1, 2))
