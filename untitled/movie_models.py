from mysql_models import MySQLConn
from mongo_models import MongoConn
from move_base import MovieBase
from config import Config

class Movie(MovieBase):
    def DBupdate(self):
        if Config.Database == Config.MySQL:
            self.DBupdateMySQL()
        else:
            self.DBupdateMongoDB()

    def DBfetchall(self, name='', actors=''):
        if Config.Database == Config.MySQL:
            return self.DBfetchallMySQL(name, actors)
        else:
            return self.DBfetchallMongoDB(name, actors)

    def DBfetchone(self, name='', actors=''):
        if Config.Database == Config.MySQL:
            return self.DBfetchoneMySQL(name, actors)
        else:
            return self.DBfetchoneMongoDB(name, actors)

    def DBdelete(self, no=''):
        if Config.Database == Config.MySQL:
            self.DBdeleteMySQL(no)
        else:
            self.DBdeleteMongoDB(no)

    def DBupdateMongoDB(self):
        mongo = MongoConn()
        x = mongo.mycol.update(
            {'no': self.no},
            {
                'no': self.no,
                'name': self.name,
                 'actors': self.actors,
                 'time': self.time,
                 'score': self.score
            }, upsert=True
        )
        print("inserted/updated:", x)

    def DBfetchallMongoDB(self, name='', actors=''):
        mongo = MongoConn()
        cur = mongo.mycol.find(
            {'$or': [{'name': {'$regex': '^' + name}}, {'actors': {'$regex': '^' + actors}}]}
        )
        # cur = mongo.mycol.find()
        movies = []
        for row in cur:
            # print(row)
            mv = Movie(no=row['no'], name=row['name'], actors=row['actors'], time=row['time'], score=row['score'])
            movies.append(mv)
        print("return list of movie objects..", movies)
        return movies

    def DBfetchoneMongoDB(self, name='', actors=''):
        mongo = MongoConn()
        row = mongo.mycol.find_one(
            {'$or': [{'name': {'$regex': '^' + name}}, {'actors': {'$regex': '^' + actors}}]}
        )
        print(row)
        # cur = mongo.mycol.find()
        mv = Movie(no=row['no'], name=row['name'], actors=row['actors'], time=row['time'], score=row['score'])
        print("return list of movie objects..", mv)
        return mv

    def DBdeleteMongoDB(self, no):
        mongo = MongoConn()
        x = mongo.mycol.delete_many({'no': no})
        print("delete..", x.deleted_count)


    def DBupdateMySQL(self):
        strsql = "SELECT count(*) FROM pymovies WHERE no=" + self.no
        # print(strsql)
        mysql = MySQLConn()
        cur = mysql.execQuery(strsql)
        strsql = ""
        if cur[0][0] == 0:
            strsql = "INSERT into pymovies (no,name,actors, time, score) VALUES("
            strsql = strsql + "" + self.no + ","
            strsql = strsql + "'" + self.name + "',"
            strsql = strsql + "'" + self.actors + "',"
            strsql = strsql + "'" + self.time + "',"
            strsql = strsql + "'" + self.score + "'"
            strsql = strsql + ")"
        else:
            strsql = "update pymovies set"
            strsql = strsql + " name ='" + self.name + "',"
            strsql = strsql + " actors='" + self.actors + "',"
            strsql = strsql + " time='" + self.time + "',"
            strsql = strsql + " score='" + self.score + "'"
            strsql = strsql + " WHERE no=" + self.no
        # print(strsql)
        mysql.execUID(strsql)
        print("{}: {}insert/update to DB".format(self.no, self.name))

    def DBfetchallMySQL(self, name='', actors=''):
        strsql = "SELECT no,name,actors,time,score FROM pymovies WHERE name like '%" + name + "%' or actors like '%" + actors + "%'"
        mysql = MySQLConn()
        cur = mysql.execQuery(strsql)
        print(cur)
        movies = []
        for row in cur:
            # print(row)
            mv = Movie(no=row[0], name=row[1], actors=row[2], time=row[3], score=row[4])
            movies.append(mv)
        print("return list of movie objects")
        return movies


    def DBfetchoneMySQL(self, name='', actors=''):
        self.name = name
        self.actors = actors
        strsql = "SELECT no,name,actors,time,score FROM pymovies WHERE name like '%" + self.name + "%' or actors like '%"+self.actors + "%' order by no  limit 1;"
        # print(strsql)
        mysql = MySQLConn()
        cur = mysql.execQuery(strsql)
        for row in cur:
            # print("row['no']:{}".format(row[0]))
            self.no = int(row[0])
            self.name = row[1]
            self.actors = row[2]
            self.score = row[3]
            self.score = row[4]
        print("return movie")
        return self

    def DBdeleteMySQL(self, no=''):
        mysql = MySQLConn()
        strsql = "DELETE FROM pymovies WHERE no="
        strsql = strsql + "" + no + ""
        # print(strsql)
        mysql.execUID(strsql)
        print("delete")


if __name__ == '__main__':
    mongo = Movie()
    x = mongo.DBfetchall()
    print(x)

