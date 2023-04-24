import re

strText = "My number is greats ddd"
regex = re.compile(r'\b\w{6}\b')  # 匹配6个字符的单词
text = regex.search(strText)
text.group()  # 调用 group() 返回结果

print(text.group())

print("#######################findall########################")

listMatch = regex.findall(strText)
print(listMatch)

for index, strMatch in enumerate(listMatch):
    print(str(index) + '--' + strMatch)

print("######################match#########################")

m = re.match(r"(\w+)\s+(\w+)", "Isaac Newton, physicist")
print(m)
print(m.group())
print(m.group(1))

tGroup = m.group(1, 2)
print(tGroup)

for strMatch in tGroup:
    print(strMatch)

print("########################search#######################")

str1 = """# print(q)  #<img src="/img.ivsky.com/im.jpg" 
alt="&#x65F6;&#x5C1A;&#x6444;&#x5F71;&#x56FE;&#x7247;"/> """
regex1 = re.compile(r'/img.+jpg')  # 匹配6个字符的单词

print(regex1.search(str1).group())

print("######################replace#########################")

url = "https://mtl.gzhuibei.com/images/img/3273/1.jpg"
finalU = re.sub(r'https.+img', "", url)
print(finalU.replace('/', ''))

print("###############################################")

showType = "1"
ss = "" if showType is None else showType

ss = re.sub(r'\s+', '', ss)

if ss is None:
    print('->none')
elif ss in {"1", "0", "-1"}:
    print("->" + "set" + ss)
elif ss != '':
    print("->" + ss)
else:
    print('->空')

print("######################match_replace#########################")
print("######################match_replace#########################")

file_str = """
	@Override
	public void onPageSelected(int idx) {
		setTab(idx);
	}
	alertDialog.setOnClick(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                alertDialog.dismiss();
                finish();
                GeneralService.getInstance().getPorting().openJYLoginActivity();//打开普通交易登录界面
            }
        });
	"""
file_str1="	public void onPageSelected(int idx) {              public void onClick(View view) {"
file_str2=""
print(re.match(r".+\s+(onClick|onPageSelected)(.+)\s*{\s*$", file_str1))
