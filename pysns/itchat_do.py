import itchat


def loginBack():
    print('微信登入')


def exitBack():
    print('微信登出')


# 登入
itchat.auto_login(hotReload=True, loginCallback=loginBack, exitCallback=exitBack)

itchat.send('你好again, filehelper', toUserName='filehelper')
print(itchat.search_friends())
