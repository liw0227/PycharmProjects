from spider_models import Spider
from movie_models import Movie


def getdatabyspider():
    print("start pull by spider......")
    i = 1
    for offset in range(0, 100, 10):
        movies = Spider.parse_url(offset=offset)

        for each_movie in movies:
            # print(each_movie['name'])
            myMovie = Movie(no=str(i), name=each_movie['name'],
                            actors=each_movie['actors'],
                            time=each_movie['time'],
                            score=each_movie['score'])
            myMovie.DBupdate()
            i = i + 1
        print("{} records inserted/updated to DB".format(i-1))


if __name__ == '__main__':
    getdatabyspider()
    print("query all............")
    mymv = Movie()
    movies = mymv.DBfetchall()
    for mv in movies:
        print("{0},{1},{2},{3}".format(mv.no,mv.name,mv.actors,mv.time,mv.score))
    print("query one............")
    mv = mymv.DBfetchone(name='霸王别姬')
    print("ONLY ONE>>>> {0},{1},{2},{3}".format(mv.no, mv.name, mv.actors, mv.time, mv.score))

    print("delete")
    mymv.DBdelete(no='1')
    movies = mymv.DBfetchall()
    for mv in movies:
        print("{0},{1},{2},{3}".format(mv.no, mv.name, mv.actors, mv.time, mv.score))