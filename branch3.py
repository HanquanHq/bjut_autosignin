# -*- coding: utf-8 -*-
import logging
import requests
import urllib3

# 禁用warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# 填写帐号密码
userAccounts = [
    #    ['username','id', 'token'],
    ['同学A昵称（此处无所谓）', '2c95xxxxxde11434017e0e2491dxxxxx（此处为同学Aid）', 'A28654074XXX2AC00A4F6C14272B80FXXXX（此处为同学Atoken）'],
    ['同学B昵称（此处无所谓）', '2c95xxxxxde11434017e0e2491dxxxxx（此处为同学Bid）', 'A28654074XXX2AC00A4F6C14272B80FXXXX（此处为同学Btoken）'],
    ['同学C昵称（此处无所谓）', '2c95xxxxxde11434017e0e2491dxxxxx（此处为同学Cid）', 'A28654074XXX2AC00A4F6C14272B80FXXXX（此处为同学Ctoken）']
]


def func(id, token):

    # 获取JSESSIONID用headers
    url1 = 'http://xgxt.bjut.edu.cn/nonlogin/qywx/authentication.htm?appId=2c95de297d4f8bfa017d8631748b7fe2&urlb64'\
            '=L3dlYkFwcC94dWVnb25nL2luZGV4Lmh0bWwjL2FjdGlvbi9iYXNlSW5kZXgvJUU3JUE3JUJCJUU1JThBJUE4JUU1JUFEJUE2JUU1JUI3JUE1'
    h1 = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
        'Connection': 'keep-alive',
        'Host': 'xgxt.bjut.edu.cn',
        'Cookie': 'id=' + id + '; token=' + token,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/85.0.4183.83 Safari/537.36 '
    }
    # 模拟GET用cookie登陆 HTTP/1.1
    r1 = requests.get(url=url1, headers=h1)
    print('r1状态码：', r1.status_code)
    setcookie = r1.history[0].headers['Set-Cookie']
    print('r1.history[0]cookie：', setcookie)
    strJSID = setcookie[:setcookie.index(';')]

    # 打卡用headers
    url2 = 'http://xgxt.bjut.edu.cn/syt/zzapply/operation.htm'
    h2 = {
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
        'Cookie': strJSID + '; id=' + id + '; token=' + token,
        'Host': 'xgxt.bjut.edu.cn',
        #'Content-length': '1150'
    }
    # 模拟POST 投寄打卡json
    r2 = requests.post(url=url2, headers=h2,
                       data='data=%7B%22xmqkb%22%3A%7B%22id%22%3A%222c95de297d4f8bfa017d85f53d267613%22%7D%2C%22c16%22%3A%22%E5%9C%A8%E6%A0%A1%E4%B8%94%E4%BD%8F%E5%AE%BF%22%2C%22c17%22%3A%22%E5%9C%A8%E4%BA%AC%22%2C%22c18%22%3A%22%E4%BD%8E%E9%A3%8E%E9%99%A9%E5%9C%B0%E5%8C%BA%22%2C%22c15%22%3A%22%E6%97%A0%E6%83%85%E5%86%B5%22%2C%22c1%22%3A%22%E5%B7%B2%E5%87%86%E7%A1%AE%E7%99%BB%E8%AE%B0%22%2C%22c12%22%3A%22%E5%8C%97%E4%BA%AC%E5%B8%82%2C%E5%8C%97%E4%BA%AC%E5%B8%82%2C%E6%9C%9D%E9%98%B3%E5%8C%BA%2C%22%2C%22type%22%3A%22YQSJSB%22%7D&msgUrl=syt%2Fzzapply%2Flist.htm%3Ftype%3DYQSJSB%26xmid%3D2c95de297d4f8bfa017d85f53d267613&uploadFileStr=%7B%7D&multiSelectData=%7B%7D&type=YQSJSB')
    print('\nr3状态码：', r2.status_code)
    # success->成功打卡 error->失败 Applied today->今天已经打过卡
    if r2.text == 'success':
        print('成功打卡')
    else:
        if r2.text == 'Applied today':
            print('今天已经打过卡')
        else:
            print('打卡失败')
    r2.close()


# process函数处理打卡和签到
def process():
    for userAccount in userAccounts:
        print('username：%s正在执行打卡' % (userAccount[0]))
        func(userAccount[1], userAccount[2])
        print('############################################################')


def handler(event, context):
  process();
