# coding=utf-8

import behave2cucumber
import json

# # 在开始全部的测试之前执行
# # 此处为打开浏览器
# def before_all(context):
#     context.dr = webdriver.Chrome()

# 在所有的测试完成之后执行
# 此处为关闭浏览器，并将behave 的json报告转化为 cucumber兼容的json报告，便于Jenkins集成展示
def after_all(context):
    # context.dr.close()
    file = r'/src/features/reports/jsonDumps/testResult.json'
    with open(file) as behave_json:
        cucumberJson = behave2cucumber.convert(json.load(behave_json))
        jsonStr = json.dumps(cucumberJson)

    jsonReport = open(r'/src/features/reports/jsonReports/jsonReport.json','w')
    jsonReport.write(jsonStr)
    jsonReport.close()