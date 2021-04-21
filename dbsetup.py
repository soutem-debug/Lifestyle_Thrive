from sqlalchemy import Column, Integer, VARCHAR, create_engine, DATETIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, nullable=False)
    user_name = Column(VARCHAR(100), nullable=False)
    user_email = Column(VARCHAR(100),unique=True ,nullable=False)
    user_pw = Column(VARCHAR(100), nullable=False)


class BlogPosts(Base):
    __tablename__ = 'blog_posts'
    post_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    post_date = Column(DATETIME, nullable=False)
    post_title = Column(VARCHAR(45), nullable=False)
    post_content = Column(VARCHAR(1000),unique=False, nullable=False)
    post_likes_count = Column(Integer, nullable=True)
    post_comment_count = Column(Integer, nullable=True)

engine = create_engine("mysql://admin2:@GitPa$$w0rd#@54.74.234.11/thefantasticfour?charset=utf8mb4")

Base.metadata.create_all(engine)
