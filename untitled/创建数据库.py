from pymysql import *

#  创建对象：调用connect()方法
# 参数host：连接的mysql主机，如果本机是'localhost'
# 参数port：连接的mysql主机的端口，默认是3306
# 参数database：数据库的名称
# 参数user：连接的用户名
# 参数password：连接的密码
# 参数charset：通信采用的编码方式，推荐使用utf8
conn=connect(host = 'localhost',
             port = 3306,
             database = 'mysql',
             user = 'root',
             password = '123456',
             charset = 'utf8'
             )


#  写入数据库
class movies:
    def __init__(self, no=0, name='', actors='', time='', score=''):
        self.no = no
        self.name = name
        self.actore = actors
        self.time = time
        self.score = score
