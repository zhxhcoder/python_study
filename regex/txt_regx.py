import re

regex = re.compile(r'\b\w{6}\b')  # 匹配6个字符的单词
text = regex.search('My number is greats')
text.group()  # 调用 group() 返回结果

print(text)

m = re.search('(?<=abc)def', 'abcdefaaadef')
print(m.group(0))
