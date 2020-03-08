import pymysql
import config
class MySQLConn:

    def __init__(self):
        self.db = pymysql.connect(config.MysqlConnectString['localhost'],
                          config.MysqlConnectString['root'],
                          config.MysqlConnectString['123456'],
                          config.MysqlConnectString['数据库管理'],
                          charset='utf8')


    def __del__(self):
        self.db.close()

    def execQuery(self, sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def execUID(self, sql):

        cursor = self.db.cursor()
        cursor.execute(sql)
        self.db.commit()
