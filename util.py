# coding=utf-8
from datetime import datetime
import MySQLdb

class DateTimeUtil:
    @staticmethod
    def getYesterday():
        today = datetime.date.today()
        oneday = datetime.timedelta(days=1)
        yesterday = today - oneday
        return yesterday

    @staticmethod
    def getToday():
        today = datetime.date.today()
        return today

    @staticmethod
    def getNowDatetime():
        nowDatetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return nowDatetime

    @staticmethod
    def getNowTime():
        nowTime = datetime.now().time()
        return nowTime

class DatabaseUtil:
    ip = "localhost"
    port = 3306
    dbName = "mscWeb"
    user = "root"
    password = "lxm19961204"
    #获取数据库connection
    @staticmethod
    def getConn():
        conn= MySQLdb.connect(
            host= DatabaseUtil.ip,
            port = DatabaseUtil.port,
            user= DatabaseUtil.user,
            passwd= DatabaseUtil.password,
            db = DatabaseUtil.dbName,
        )
        return conn


    @staticmethod
    def getCursor():
        conn = DatabaseUtil.getConn()
        cur = conn.cursor()
        return cur

    #建表
    @staticmethod
    def createTable():
        cur = DatabaseUtil.getCursor()
        print "ok"

        # tablename = "user_table"
        # sql = """CREATE TABLE """+tablename+""" (
        # user_id BIGINT primary key not null auto_increment
        # )"""
        # cur.execute(sql)

        # tablename = "post_table"
        # sql = """CREATE TABLE """+tablename+""" (
        # post_id BIGINT primary key not null auto_increment ,
        # author_id BIGINT not null,
        # title  varchar(100) not null,
        # content text not null,
        # create_time datetime not null,
        # update_time datetime not null,
        # viewCount int not null default 0,
        # saveCount int not null default 0,
        # replyCount int not null default 0,
        # is_solved tinyint not null default 0
        # )"""
        # cur.execute(sql)

        # tablename = "reply_table"
        # sql = """CREATE TABLE """+tablename+""" (
        # reply_id BIGINT primary key not null auto_increment ,
        # author_id BIGINT not null,
        # content text not null,
        # create_time datetime not null,
        # update_time datetime not null,
        # likeCount int not null default 0,
        # commentCount int not null default 0,
        # bePicked tinyint not null default 0
        # )"""
        # cur.execute(sql)
        #
        # tablename = "comment_table"
        # sql = """CREATE TABLE """+tablename+""" (
        # comment_id BIGINT primary key not null auto_increment ,
        # author_id BIGINT not null,
        # content text not null,
        # create_time datetime not null,
        # likeCount int not null default 0
        # )"""
        # cur.execute(sql)

        # tablename = "post_reply_table"
        # sql = """CREATE TABLE """+tablename+""" (
        # post_id BIGINT not null,
        # reply_id BIGINT not null,
        # primary key(post_id,reply_id),
        # foreign key(post_id) references post_table(post_id) on delete cascade,
        # foreign key(reply_id) references reply_table(reply_id) on delete cascade
        # )"""
        # cur.execute(sql)

        # tablename = "post_comment_table"
        # sql = """CREATE TABLE """+tablename+""" (
        # post_id BIGINT not null,
        # comment_id BIGINT not null,
        # primary key(post_id,comment_id),
        # foreign key(post_id) references post_table(post_id) on delete cascade,
        # foreign key(comment_id) references comment_table(comment_id) on delete cascade
        # )"""
        # cur.execute(sql)
        #
        # tablename = "reply_comment_table"
        # sql = """CREATE TABLE """+tablename+""" (
        # reply_id BIGINT not null,
        # comment_id BIGINT not null,
        # primary key(reply_id,comment_id),
        # foreign key(reply_id) references reply_table(reply_id) on delete cascade,
        # foreign key(comment_id) references comment_table(comment_id) on delete cascade
        # )"""
        # cur.execute(sql)
        #
        # tablename = "comment_comment_table"
        # sql = """CREATE TABLE """+tablename+""" (
        # comment_parent_id BIGINT not null,
        # comment_child_id BIGINT not null,
        # primary key(comment_parent_id,comment_child_id),
        # foreign key(comment_parent_id) references comment_table(comment_id) on delete cascade,
        # foreign key(comment_child_id) references comment_table(comment_id) on delete cascade
        # )"""
        # cur.execute(sql)
        #
        # tablename = "viewRecord_table"
        # sql = """CREATE TABLE """+tablename+""" (
        # user_id BIGINT not null,
        # post_id BIGINT not null,
        # primary key(user_id,post_id),
        # foreign key(user_id) references user_table(user_id) on delete cascade,
        # foreign key(post_id) references post_table(post_id) on delete cascade
        # )"""
        # cur.execute(sql)
        #
        # tablename = "saveRecord_table"
        # sql = """CREATE TABLE """+tablename+""" (
        # user_id BIGINT not null,
        # post_id BIGINT not null,
        # primary key(user_id,post_id),
        # foreign key(user_id) references user_table(user_id) on delete cascade,
        # foreign key(post_id) references post_table(post_id) on delete cascade
        # )"""
        # cur.execute(sql)
        #
        # tablename = "likePostRecord_table"
        # sql = """CREATE TABLE """+tablename+""" (
        # user_id BIGINT not null,
        # post_id BIGINT not null,
        # primary key(comment_parent_id,comment_child_id),
        # foreign key(user_id) references user_table(user_id) on delete cascade,
        # foreign key(post_id) references comment_table(comment_id) on delete cascade
        # )"""
        # cur.execute(sql)

        # tablename = "likeReplyRecord_table"
        # sql = """CREATE TABLE """+tablename+""" (
        # user_id BIGINT not null,
        # reply_id BIGINT not null,
        # primary key(user_id,reply_id),
        # foreign key(user_id) references user_table(user_id) on delete cascade,
        # foreign key(reply_id) references reply_table(reply_id) on delete cascade
        # )"""
        # cur.execute(sql)
        #
        # tablename = "likeCommentRecord_table"
        # sql = """CREATE TABLE """+tablename+""" (
        # user_id BIGINT not null,
        # comment_id BIGINT not null,
        # primary key(user_id,comment_id),
        # foreign key(user_id) references user_table(user_id) on delete cascade,
        # foreign key(comment_id) references comment_table(comment_id) on delete cascade
        # )"""
        # cur.execute(sql)

# DatabaseUtil.createTable()
