from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "替换成你的ACCOUNT_SID"
# Your Auth Token from twilio.com/console
auth_token = "替换成你的auth_token"
client = Client(account_sid, auth_token)
message = client.messages.create(
    to="+86xxxxxxxxxxx,替换成注册的手机号，也就是要接收短信的手机号，中国区是+86",
    from_="+15017250604，替换成你的twilio phone number，twilio分配给你的",
    body="Hello from Python Twilio!")
