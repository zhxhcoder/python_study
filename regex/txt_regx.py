import re

regex = re.compile(r'\b\w{6}\b')  # 匹配6个字符的单词
regex.search('My phone number is 421-2343-121')
text = regex.search('My phone number is 421-2343-121')
text.group()  # 调用 group() 返回结果

print(text.group())
