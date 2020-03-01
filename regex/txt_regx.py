import re

strText = "My number is greats ddd"
regex = re.compile(r'\b\w{6}\b')  # 匹配6个字符的单词
text = regex.search(strText)
text.group()  # 调用 group() 返回结果

print(text.group())

print("###############################################")

listMatch = regex.findall(strText)
print(listMatch)

for index, strMatch in enumerate(listMatch):
    print(str(index) + '--' + strMatch)

print("###############################################")

m = re.match(r"(\w+)\s+(\w+)", "Isaac Newton, physicist")
print(m.group())
print(m.group(1))

tGroup = m.group(1, 2)
print(tGroup)

for strMatch in tGroup:
    print(strMatch)

print("###############################################")

str1="""# print(q)  #<img src="/img.ivsky.com/im.jpg" 
alt="&#x65F6;&#x5C1A;&#x6444;&#x5F71;&#x56FE;&#x7247;"/> """
regex1 = re.compile(r'/img.+jpg')  # 匹配6个字符的单词

print(regex1.search(str1).group())