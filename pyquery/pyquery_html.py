from pyquery import PyQuery as pq

html = """
<html lang="en">
    <head>
        简单好用的
        <title>PyQuery</title>
    </head>
    <body>
        <ul id="container">
            <li class="object-1">Python</li>
            <li class="object-2">大法</li>
            <li class="object-3">好</li>
        </ul>
    </body>
</html>
"""

# 初始化为PyQuery对象
doc = pq(html)
print(type(doc))
print(doc)
