# coding:utf-8
import requests
from wheel.signatures import assertTrue
import sys
import simplejson
from behave import *


sys.path.append("/Users/garen/dev/pyspeces/auto_test")
scene = 1


bitexUrl = "https://x-agent.i-counting.cn/api/v1/security/login"
head = {'content-type':'application/json'}



@Given(':测试者输入用户名{UserName},密码{UserPassWord},用例名称是:{caseName}')
def step_impl(context, UserName, UserPassWord, caseName):
    context.caseName = caseName
    context.UserName = UserName
    context.UserPassWord = UserPassWord
    print("用例",scene,context.caseName + '\n')



@When(':输入参数完毕后并成功发送请求')
def step_im(context):
    respones = userLogin(context.UserName,context.UserPassWord)
    context.respones = simplejson.loads(respones)
    print(type(context.respones))



@Then(':接口返回的状态是{status},错误代码{errorCode},错误信息{errorMsg}')
def step_impl(context,status,errorCode,errorMsg):
    global scene
    scene += 1

    print("接口响应",context.respones,"\n")

    context.status = status

    print(context.status)

    assertTrue(context.status,context.respones.get('status'))


def userLogin(userName,loginPwd):
    payload = {
        "UserName": userName,
        "UserPassWord": loginPwd
    }
    respones = requests.post(bitexUrl,data=simplejson.dumps(payload),headers=head)
    str_dict = simplejson.loads(respones.text)
    return str_dict
