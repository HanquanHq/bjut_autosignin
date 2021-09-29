##疫情通每日打卡
##autosignin是什么?
一个基于python3的批量自动打卡脚本 //可能仅限于BJUT？


##有问题反馈
在使用中有任何问题，欢迎在issue区反馈给我

branch1 为知道bjut.sanyth.com 密码时使用（部分同学密码和xgxt.bjut.edu.cn相同
branch2 （推荐）使用的是有效期一周的ID和TOKEN，通过抓包企业微信打卡很容易获得

建议环境：
```
python3.8
```
此脚本POST用到的打卡包可以直接使用，脚本中预先填写好的
也可自己填写并转换为raw。

另外：
脚本核心就是branch1和branch2，
关于批量打卡部分可以按照下面这样：
```python
# process函数处理打卡和签到
userAccounts = [
#   ['username', 'id' , 'token' ],  #此处是branch2的，branch1稍加修改即可
    ['example1', 'XXX', 'XXXXXX'],
    ['example2', 'XXX', 'XXXXXX'],
    ...
]
def process():
    for userAccount in userAccounts:
        print('username：%s正在执行打卡' % (userAccount[0]))
        func(userAccount[1], userAccount[2])          #此处调用的func()就是脚本的主体部分
        print('############################################################')
```
再另外：
如果你用的是branch1那种方法，注意username和password要用base64转码后才可以（）
```python
import base64
u = base64.b64encode(username.encode('utf-8')).decode('utf-8')
p = base64.b64encode(pwd.encode('utf-8')).decode('utf-8')
