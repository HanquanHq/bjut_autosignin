import base64
import json
import os
import urllib

import requests
import urllib3
import urllib.request
from urllib.parse import quote, unquote

# 禁用warning
from PIL import Image

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# 填写帐号密码
userAccounts = [
    #    ['userStudentId', 'password'],
    ['19010101', '123456']
]


def func(username, pwd):
    # 初始化用headers
    url1 = 'http://xgxt.bjut.edu.cn/'
    h1 = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
        'Connection': 'keep-alive',
        'Host': 'xgxt.bjut.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/85.0.4183.83 Safari/537.36 '
    }
    # 模拟GET HTTP/1.1
    r1 = requests.get(url=url1)
    print('r1状态码：', r1.status_code)
    setcookie = r1.headers['Set-Cookie']
    print(setcookie)
    print('r1cookie：', setcookie)
    strJSID = setcookie[:setcookie.index(';')]
    token = setcookie[setcookie.index(',') + 8:setcookie.index('; Expires')]

    # 获取验证码用headers
    url1_1 = 'http://xgxt.bjut.edu.cn/nonlogin/login/captcha.htm'
    h1_1 = {
        'Accept': 'image/webp,image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': strJSID,
        'Host': 'xgxt.bjut.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/85.0.4183.83 Safari/537.36 '
    }
    # 模拟GET HTTP/1.1
    r1_1 = requests.get(url=url1_1, headers=h1_1)
    print('r1_1状态码：', r1.status_code)
    os.makedirs('./image/', exist_ok=True)
    with open('./image/img.JFIF', 'wb') as f:
        f.write(r1_1.content)
#此处开始调用验证码识别api
    host = 'http://codevirify.market.alicloudapi.com'
    path = '/icredit_ai_image/verify_code/v1'
    appcode = 'xxxxxxx'
    url = host + path
    bodys = {}
    with open(r'./image/img.JFIF', 'rb') as f:
        contents = base64.b64encode(f.read())
    bodys['IMAGE'] = contents
    bodys['IMAGE_TYPE'] = '0'
    post_data = urllib.parse.urlencode(bodys).encode('utf-8')
    request = urllib.request.Request(url, post_data)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    yzm = json.loads(content.decode('utf-8'))['VERIFY_CODE_ENTITY']['VERIFY_CODE']
    print(yzm)
    # 登陆用headers
    url2 = 'http://xgxt.bjut.edu.cn//login/Login.htm'
    h2 = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': strJSID,
        'Host': 'xgxt.bjut.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/85.0.4183.83 Safari/537.36 '
    }

    u = base64.b64encode(username.encode('utf-8')).decode('utf-8')
    p = base64.b64encode(pwd.encode('utf-8')).decode('utf-8')
    loginData = {
        'username': u,
        'password': p,
        'verification': yzm,
        'token': token
    }
    # 模拟POST 登陆
    r2 = requests.post(url=url2, headers=h2, data=loginData)
    print('\nr2状态码：', r2.status_code)
    print('r2headers：', r2.headers)
    r2_1 = requests.get(url='http://xgxt.bjut.edu.cn/nonlogin/login/isLogin.htm', headers=h2)
    print('是否成功登陆', r2_1.content)

    # 打卡用headers
    url3 = 'http://xgxt.bjut.edu.cn:80/syt/zzapply/operation.htm'
    h3 = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Origin': 'http://xgxt.bjut.edu.cn',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                      'like Gecko)  Mobile/15E148 wxwork/3.1.16 MicroMessenger/7.0.1 Language/zh ColorScheme/Dark',
        'Referer': 'http://xgxt.bjut.edu.cn/webApp/xuegong/index.html',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'menuVisible=1; username=' + username + '; ' + strJSID,
        'Host': 'xgxt.bjut.edu.cn',
        'Content-length': '1204'
    }
    data3 = quote(
        'data={"xmqkb":{"id":"2c95de297d4f8bfa017d85f53d267613"},"c16":"在校且住宿","c17":"在京","c18":"低风险地区","c15":"无情况","c1":"已准确登记","location_address":"北京市朝阳区平乐园100号北京工业大学","type":"YQSJSB"}&msgUrl=syt/zzglappro/index.htm?type=yqsjsb&xmid=2c95de297d4f8bfa017d85f53d267613&multiSelectData={}')
    data3 = data3.replace('%3D', '=')
    # 模拟POST 投寄打卡json
    r3 = requests.post(url=url3, headers=h3,
                       data=data3
                       )
    print(data3)
    print('\nr3状态码：', r3.status_code)
    # success->成功打卡 error->失败 Applied today->今天已经打过卡
    if r3.text == 'success':
        print('成功打卡')
    else:
        if r3.text == 'Applied today':
            print('今天已经打过卡')
        else:
            print('打卡失败')
    r3.close()


# process函数处理打卡和签到
def process():
    for userAccount in userAccounts:
        print('username：%s正在执行打卡' % (userAccount[0]))
        func(userAccount[0], userAccount[1])


# main函数调用process
if __name__ == '__main__':
    process()
