#language: zh-CN
功能: 测试噼里啪智能财税系统

  场景大纲:测试噼里啪智能财税系统用户登陆接口
    假如:测试者输入用户名<UserName>,密码<UserPassWord>,用例名称是:<caseName>
    当:输入参数完毕后并成功发送请求
    那么:接口返回的状态是<status>,错误代码<errorCode>,错误信息<errorMsg>

    例子:
      | caseName             | UserName | UserPassWord | status | errorCode | errorMsg |
      | 登录正确的用户名密码           | likexin  | 111111       | True   | ' '       | ' '      |
      | 登录用户名或密码错误（密码错误）     | likexin  | 222222       | False  | ' '       | ' '      |
      | 登录用户名或密码错误（用户名错误）    | test     | 111111       | False  | ''        | ''       |
      | 登录用户名或密码为空（用户名、密码错误） | test     | 123456       | False  | ''        | ''       |
      | 登录用户名或密码为空（用户名为空）    | null     | 111111       | False  | ''        | ''       |
      | 登录用户名或密码为空（密码为空）     | likexin  | null         | False  | ''        | ''       |
      | 登录用户名或密码为空（用户名、密码为空） | null     | null         | False  | ''        | ''       |

