# coding=utf-8
from util import *
from Modal import *
#用户操作
class UserOperation:
    tablename = "user_table"
#原创帖操作
class PostOperation:
    tablename = "post_table"
    #取得连接
    conn = DatabaseUtil.getConn()
    cursor = conn.cursor()
    ##################query##################
    #获取所有post
    @staticmethod
    def fetchAll():
        sql = "select * from %s"%PostOperation.tablename
        # print sql
        PostOperation.cursor.execute(sql)
        results = PostOperation.cursor.fetchall()
        all_post_array=[]
        for row in results:
            post_id = row[0]
            author_id = row[1]
            title = row[2]
            content = row[3]
            create_time = row[4]
            update_time = row[5]
            viewCount = row[6]
            saveCount = row[7]
            replyCount = row[8]
            is_solved = row[9]
            post = PostModal(post_id,author_id,title,content,create_time,update_time,viewCount,saveCount,replyCount,is_solved)
            all_post_array.append(post)
        return all_post_array
    #根据id获取post
    @staticmethod
    def fetchById(post_id):
        sql = "select * from %s"%PostOperation.tablename+" where post_id = %s" %(post_id)
        # print sql
        PostOperation.cursor.execute(sql)
        results = PostOperation.cursor.fetchall()
        post_array=[]
        for row in results:
            post_id = row[0]
            author_id = row[1]
            title = row[2]
            content = row[3]
            create_time = row[4]
            update_time = row[5]
            viewCount = row[6]
            saveCount = row[7]
            replyCount = row[8]
            is_solved = row[9]
            post = PostModal(post_id,author_id,title,content,create_time,update_time,viewCount,saveCount,replyCount,is_solved)
            post_array.append(post)
        return post_array
    #根据post信息获取其id
    @staticmethod
    def fetchPostId(post):
        author_id = post.author_id
        create_time = post.create_time
        sql = "select * from %s"%PostOperation.tablename+" where author_id = %s and create_time = \'%s\'" % (post.author_id, post.create_time)
        # print sql
        PostOperation.cursor.execute(sql)
        results = PostOperation.cursor.fetchall()
        row = results[0]
        #合成对象
        post_id = row[0]
        return post_id
    ##################insert##################
    #新增，发布一个post
    @staticmethod
    def insert(post):
        author_id = post.author_id
        title = post.title
        content = post.content
        create_time = post.create_time
        update_time = post.update_time
        sql = "insert into %s"%PostOperation.tablename+" (author_id, title, content, create_time, update_time) values(%s,\'%s\',\'%s\',\'%s\',\'%s\')" % (author_id, title, content, create_time, update_time)
        # print sql
        try:
            # 执行sql语句
            PostOperation.cursor.execute(sql)
            # 提交到数据库执行
            PostOperation.conn.commit()
        except:
            # Rollback in case there is any error
            PostOperation.conn.rollback()
    ##################update##################

    ##################delete##################
    @staticmethod
    def deletePost(post_id):
        sql = "delete from %s"%PostOperation.tablename+" where post_id = %s"%post_id
        print sql
        try:
            # 执行sql语句
            PostOperation.cursor.execute(sql)
            # 提交到数据库执行
            PostOperation.conn.commit()
        except:
            # Rollback in case there is any error
            PostOperation.conn.rollback()
#跟帖操作
class ReplyOperation:
    tablename = "reply_table"
    #取得连接
    conn = DatabaseUtil.getConn()
    cursor = conn.cursor()
    ##################query##################
    ##################insert##################
    ##################update##################
    ##################delete##################
#评论操作
class CommentOperation:
    tablename = "comment_table"
    #取得连接
    conn = DatabaseUtil.getConn()
    cursor = conn.cursor()
    ##################query##################
    ##################insert##################
    ##################update##################
    ##################delete##################
#原创帖-跟帖操作
class PostReplyOperation:
    tablename = "post_reply_table"
    #取得连接
    conn = DatabaseUtil.getConn()
    cursor = conn.cursor()
    ##################query##################
    ##################insert##################
    ##################update##################
    ##################delete##################
#原创帖-评论操作
class PostCommentOperation:
    tablename = "post_comment_table"
    #取得连接
    conn = DatabaseUtil.getConn()
    cursor = conn.cursor()
    ##################query##################
    ##################insert##################
    ##################update##################
    ##################delete##################
#跟帖——评论操作
class ReplyCommentOperation:
    tablename = "reply_comment_table"
    #取得连接
    conn = DatabaseUtil.getConn()
    cursor = conn.cursor()
    ##################query##################
    ##################insert##################
    ##################update##################
    ##################delete##################
#评论-评论操作
class CommentCommentOperation:
    tablename = "comment_comment_table"
    #取得连接
    conn = DatabaseUtil.getConn()
    cursor = conn.cursor()
    ##################query##################
    ##################insert##################
    ##################update##################
    ##################delete##################
#浏览记录操作
class viewRecordOperation:
    tablename = "viewRecord_table"
    #取得连接
    conn = DatabaseUtil.getConn()
    cursor = conn.cursor()
    ##################query##################
    ##################insert##################
    ##################update##################
    ##################delete##################
#收藏夹操作
class saveRecordOperation:
    tablename = "saveRecord_table"
    #取得连接
    conn = DatabaseUtil.getConn()
    cursor = conn.cursor()
    ##################query##################
    ##################insert##################
    ##################update##################
    ##################delete##################
#点赞原创帖操作
class likePostOperation:
    tablename = "likePostRecord_table"
    #取得连接
    conn = DatabaseUtil.getConn()
    cursor = conn.cursor()
    ##################query##################
    ##################insert##################
    ##################update##################
    ##################delete##################
#点赞跟帖操作
class likeReplyOperation:
    tablename = "likeReplyRecord_table"
    #取得连接
    conn = DatabaseUtil.getConn()
    cursor = conn.cursor()
    ##################query##################
    ##################insert##################
    ##################update##################
    ##################delete##################
#点赞评论操作
class likeCommentOperation:
    tablename = "likeCommentRecord_table"
    #取得连接
    conn = DatabaseUtil.getConn()
    cursor = conn.cursor()
    ##################query##################
    ##################insert##################
    ##################update##################
    ##################delete##################
