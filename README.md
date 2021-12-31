# 严禁用于非法用途（包括但不限于虚假定位信息、健康信息）！
# 此REPO仅作为学习交流之用！
## 小更新12/31
ADD branch1_withCaptcha.py 用来适配外网访问并打卡

较branch1.py增加了识别并填充验证码功能（识别功能以调用aliyun的API为例，API部分请同学自行替换）

PS：使用校内网打卡的同学继续使用branch1.py即可（校内网打卡正常是无验证码的）
## **更新12/31 2nd**
最近xgxt又能用了，于是还可以使用branch1.py进行打卡（免去每周抓包）（branch1.py已更新适配最新打卡系统）

PS：学工系统 用户名为学号，密码为123456（默认）或网关密码 （（这两个都不行的话，自己找辅导员重置密码

## **更新12/31**
由于考试周，近期一直没更新脚本

这两天辅导员又开始催打卡了（悲

于是再次上线修改一下

现在我把我现在自用的在aliyun部署的的脚本作为branch3.py上传（偷个懒

请自行结合之前的进行修改
## 紧急更新10/29
这次系统升级了，表单有了变化

适用本脚本时请替换post data的内容

method1: 自己抓包，把data copy过来即可

method2: 自行修改表单内容按如下格式，并进行url编码encoding后，替换掉脚本中原来的data部分
```json
{"xmqkb":{"id":"402880c97b1c114b017b1c2af13d02d8"},"c15":"无情况","c16":"在校且住宿","c17":"在京","c18":"低风险地区","c12":"北京市,北京市,朝阳区,","type":"YQSJSB","location_longitude":116.21161177441111,"location_latitude":39.98611115356111,"location_address":"北京市朝阳区平乐园100号北京工业大学"}
```
ps：此处的id为appID，所有人都一样无需修改，你只需要修改地点、经纬度和个人情况即可。

method3：<懒人包>使用下面的内容替换
```
data=%7B%22xmqkb%22%3A%7B%22id%22%3A%22402880c97b1c114b017b1c2af13d02d8%22%7D%2C%22c15%22%3A%22%E6%97%A0%E6%83%85%E5%86%B5%22%2C%22c16%22%3A%22%E5%9C%A8%E6%A0%A1%E4%B8%94%E4%BD%8F%E5%AE%BF%22%2C%22c17%22%3A%22%E5%9C%A8%E4%BA%AC%22%2C%22c18%22%3A%22%E4%BD%8E%E9%A3%8E%E9%99%A9%E5%9C%B0%E5%8C%BA%22%2C%22c12%22%3A%22%E5%8C%97%E4%BA%AC%E5%B8%82%2C%E5%8C%97%E4%BA%AC%E5%B8%82%2C%E6%9C%9D%E9%98%B3%E5%8C%BA%2C%22%2C%22type%22%3A%22YQSJSB%22%2C%22location_longitude%22%3A116.21161177441111%2C%22location_latitude%22%3A39.98611115356111%2C%22location_address%22%3A%22%E5%8C%97%E4%BA%AC%E5%B8%82%E6%9C%9D%E9%98%B3%E5%8C%BA%E5%B9%B3%E4%B9%90%E5%9B%AD100%E5%8F%B7%E5%8C%97%E4%BA%AC%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6%22%7D&msgUrl=syt%2Fzzapply%2Flist.htm%3Ftype%3DYQSJSB%26xmid%3D402880c97b1c114b017b1c2af13d02d8&uploadFileStr=%7B%7D&multiSelectData=%7B%7D&type=YQSJSB
```

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

ps：笔者写这个脚本最初目的就是练习一下抓包和requests库使用，水平实在不高存在很多纰漏，欢迎各路大神随意加以开发，笔者不保留代码的任何权利，同时呼吁大家把自己改良后的代码也分享出来共同促进！
