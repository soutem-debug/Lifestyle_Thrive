
from sqlalchemy import Column, Integer, VARCHAR, create_engine, DATETIME, ForeignKey, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, nullable=False)
    user_name = Column(VARCHAR(100), nullable=False)
    user_email = Column(VARCHAR(100),unique=True,nullable=False)
    user_pw = Column(VARCHAR(100), nullable=False)



class BlogPosts(Base):
    __tablename__ = 'blog_posts'
    post_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    post_date = Column(DATETIME, nullable=False)
    post_title = Column(VARCHAR(45), nullable=False)
    post_content = Column(VARCHAR(1000),unique=False, nullable=False)
    post_likes_count = Column(Integer, nullable=True)
    post_comment_count = Column(Integer, nullable=True)




engine = create_engine("mysql+mysqlconnector://admin2:@GitPa$$w0rd#@54.74.234.11/thefantasticfour?charset=utf8mb4")


Base.metadata.create_all(engine)


class Comment(Base):
    __tablename__ = 'comments'
    comment_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    comment_date = Column(TIMESTAMP)
    comment_content = Column(VARCHAR(100), nullable=False)
    comment_like_count = Column(Integer, nullable=True)


    def __repr__(self):
        return f'<Comment %r>' % self.username % self.timestamp


class Reply(Base):
    __tablename__ = 'reply'
    reply_id = Column(Integer, primary_key=True, autoincrement=True)
    comment_id = Column(Integer, ForeignKey('comment_id'))
    post_id = Column(Integer, ForeignKey('post_id'))
    reply_content = Column(VARCHAR(100), nullable=False)
    created_at = Column(TIMESTAMP)

    def add_reply(self, text):
        return Comment(text=text, parent=self)



