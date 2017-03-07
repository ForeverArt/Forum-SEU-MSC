#_*_ coding: utf-8_*_

#author lxm
#startDate 2017/2/13
#finishDate

#tornado import
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import os
from tornado.options import define, options

#functional import
import MySQLdb
from util import *
from Modal import *
from DatabaseOperation import *

#define port : localhost
define('port',default=8000,type = int)

#
class ForumHandler(tornado.web.RequestHandler):
    def get(self):
        postArray = PostOperation.fetchAll()
        self.render('forum.html',postArray = postArray)

#
class PostHandler(tornado.web.RequestHandler):
    def get(self,post_id):
        postId = int(post_id)
        post = PostOperation.fetchById(postId)
        self.render('post.html',post = post)

class PublishHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('write.html')
    def post(self):
        post_id = -999
        # author_id = self.get_argument("author_id")
        # for adding post to test
        author_id = 7;
        title = self.get_argument("title")
        content = self.get_argument("content")
        create_time = DateTimeUtil.getNowDatetime()
        update_time = create_time
        viewCount = 0
        saveCount = 0
        replyCount = 0
        is_solved = 0
        post = PostModal(post_id,author_id,title,content,create_time,update_time,viewCount,saveCount,replyCount,is_solved)
        PostOperation.insert(post)
        post.post_id = PostOperation.fetchPostId(post)
        self.render('published.html', post = post)

class PersonalHandler(tornado.web.RequestHandler):
    def get(self,user_id):
        self.render('personal.html')
    def post(self,user_id):
        # self look
        self.render('personal.html')


#setting
if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
            handlers=[
                (r'/forum',ForumHandler),
                (r'/post/([0-9]+)',PostHandler),
                (r'/publish',PublishHandler),
                (r'/personal/([0-9]+)',PersonalHandler),
            ],
            template_path=os.path.join(os.path.dirname(__file__),'templates'),
            static_path=os.path.join(os.path.dirname(__file__),'static')
            )

#api for database
# def connectToMysql():
#     conn = pymongo.Connection("localhost", 27017)


#basic start
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(options.port)
tornado.ioloop.IOLoop.instance().start()
#connect database
# connectToMysql()
