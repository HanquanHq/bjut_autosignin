## 疫情通每日打卡
## autosignin是什么?
一个基于python3的批量自动打卡脚本 //可能仅限于BJUT？


## 有问题反馈
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
```
10.1更新：有同学问我白嫖阿里云函数服务怎么搞 ， 我简要说明下哈
（搞完之后，就可以完全脱管了，设置每天某一固定时间服务器帮你准时打卡）
（白嫖：阿里云每个月给你数万次的调用函数免费额度，实际打卡一个月的计算量根本用不完，所以可以称之为“白嫖”）
阿里云函数计算FC 选择python3容器然后将修改后的branch2代码完全覆盖进去
阿里云函数计算是把handler做为入口，所以只要在branch2代码添加个handler()函数进去即可
可以像我这样：
```python
def handler(event, context):
  process(); #此处调用的函数名填写你实际想调用的那个函数即可
```
另外说明一下，触发器的设置
进入函数详情->触发器管理->添加触发器->触发器类型：定时触发器->触发方式：按cron表达式触发
然后填入你想要自定义的cron表达式即可
（阿里云cron时区是UTC时间，比北京时间慢8小时
也就是说你想要每天北京时间8点打卡，你要设置成0点）
cron表达式可以像我这样写：
```
0 0 0 * * ?
```

更新： 这位朋友对脚本做了些有益的补充,若是修改打卡信息等出现问题或许可以查看一下他的解决方案，请移步<https://github.com/galaxyxxxxx/auto-clock-in>。
