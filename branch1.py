import requests
import urllib3
import base64

# 禁用warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def func():
    # 初始化用headers
    # noinspection HttpUrlsUsage
    url1 = 'http://bjut.sanyth.com:81/'
    h1 = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
        'Connection': 'keep-alive',
        'Host': 'bjut.sanyth.com:81',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/85.0.4183.83 Safari/537.36 '
    }
    # 模拟GET HTTP/1.1
    r1 = requests.get(url=url1, headers=h1)
    print('r1状态码：', r1.status_code)
    setcookie = r1.headers['Set-Cookie']
    print('r1cookie：', setcookie)
    strJSID = setcookie[:setcookie.index(';')]
    token = setcookie[setcookie.index(',') + 8:setcookie.index('; Max')]

    # 登陆用headers
    url2 = 'http://bjut.sanyth.com:81//login/Login.htm'
    h2 = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': strJSID,
        'Host': 'bjut.sanyth.com:81',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/85.0.4183.83 Safari/537.36 '
    }
    username='XXXXX' #此处输入用户名
    pwd='XXXXX' #此处输入密码
    u = base64.b64encode(username.encode('utf-8')).decode('utf-8')
    p = base64.b64encode(pwd.encode('utf-8')).decode('utf-8')
    loginData = {
        'username': u,
        'password': p,
        'verification': '',
        'token': token
    }
    # 模拟POST 登陆
    r2 = requests.post(url=url2, headers=h2, data=loginData)
    print('\nr2状态码：', r2.status_code)
    #print('r2headers：', r2.headers)
    print(r2.content)

    id_siginin='XXXXX' #此处输入打卡id （可通过抓包
    token_signin='XXXXX' #此处输入打卡token （可通过抓包
    # 打卡用headers
    url3 = 'http://bjut.sanyth.com:81/syt/zzapply/operation.htm'
    h3 = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Origin': 'http://bjut.sanyth.com:81',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                      'like Gecko)  Mobile/15E148 wxwork/3.1.16 MicroMessenger/7.0.1 Language/zh ColorScheme/Dark',
        'Referer': 'http://bjut.sanyth.com:81/webApp/xuegong/index.html',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': strJSID + '; id='+id_siginin+'; token='+token_signin,
        'Host': 'bjut.sanyth.com:81',
        'Content-length': '1204'
    }
    # 模拟POST 投寄打卡json
    r3 = requests.post(url=url3, headers=h3,
                       data='data=%7B%22xmqkb%22%3A%7B%22id%22%3A%22402880c97b1c114b017b1c2af13d02d8%22%7D%2C%22c1%22'
                            '%3A%22%E5%9C%A8%E7%B1%8D%E6%9C%AC%E7%A7%91%E7%94%9F%22%2C%22c2%22%3A%22%E5%9C%A8%E6%A0'
                            '%A1%E5%86%85%E5%B1%85%E4%BD%8F%22%2C%22c3%22%3A%22%E5%90%A6%22%2C%22c4%22%3A%22%E5%90%A6'
                            '%22%2C%22c5%22%3A%22%E6%AD%A3%E5%B8%B8%22%2C%22c6%22%3A%22%E6%AD%A3%E5%B8%B8%22%2C%22c7'
                            '%22%3A%22%E6%97%A0%E6%83%85%E5%86%B5%22%2C%22c8%22%3A%22%E5%9C%A8%E4%BA%AC%E5%86%85%22'
                            '%2C%22c12%22%3A%22%E5%8C%97%E4%BA%AC%E5%B8%82%2C%E5%8C%97%E4%BA%AC%E5%B8%82%2C%E6%9C%9D'
                            '%E9%98%B3%E5%8C%BA%2C%22%2C%22c9%22%3A%22%E5%90%A6%22%2C%22c10%22%3A%22%E5%90%A6%22%2C'
                            '%22c11%22%3A%22%E5%90%A6%22%2C%22c14%22%3A%22%E5%B7%B2%E5%85%A8%E7%A8%8B%E6%8E%A5%E7%A7'
                            '%8D%22%2C%22type%22%3A%22YQSJSB%22%2C%22location_longitude%22%3A116.48137725683594%2C'
                            '%22location_latitude%22%3A39.87708184838867%2C%22location_address%22%3A%22%E5%8C%97%E4'
                            '%BA%AC%E5%B8%82%E6%9C%9D%E9%98%B3%E5%8C%BA%E5%8D%97%E7%A3%A8%E6%88%BF%E4%B9%A1%E5%8C%97'
                            '%E4%BA%AC%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6%22%7D&msgUrl=syt%2Fzzapply%2Flist.htm'
                            '%3Ftype%3DYQSJSB%26xmid%3D402880c97b1c114b017b1c2af13d02d8&uploadFileStr=%7B%7D'
                            '&multiSelectData=%7B%7D&type=YQSJSB')
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


if __name__ == '__main__':
    func()
