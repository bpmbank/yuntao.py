#coding=utf8
import tornado
from yuntao import log
from yuntao import dates
from business import common
import json
class ReadRss(tornado.web.RequestHandler):
    def get(self):
        dao = common.getdao()
        datas = dao.query("select * from rss_article order by pubdate desc limit 20");
        for data in datas:
            data["description"] = data.description.strip()[0:30]
            data["pubdate"] = dates.datetime2str(data.pubdate)
        result = {"success":True,"data":datas}
        self.set_header("Content-Type","text/json")
        self.write(json.dumps(result))
        self.finish()

class ReadArticle(tornado.web.RequestHandler):
    def get(self,article_id):
        datas =  common.getdao().query("select title,description from rss_article where id=%s",article_id);
        result = {"success":True,"data":datas[0]}
        self.set_header("Content-Type","text/json")
        self.write(json.dumps(result))
        self.finish()