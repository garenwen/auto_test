# coding:utf-8


import requests,simplejson
bitexUrl = "https://x-agent.i-counting.cn/api/v1/security/login"
head = {'content-type':'application/json'}

# 用户登录
def userLogin(userName,loginPwd):
    payload = {
        "UserName": userName,
        "UserPassWord": loginPwd
    }
    respones = requests.post(bitexUrl,data=simplejson.dumps(payload),headers=head)
    str_dict = simplejson.loads(respones.text)
    return str_dict