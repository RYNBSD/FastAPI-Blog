from sqlalchemy import Column, ForeignKey, String, BigInteger, UUID, DateTime
from uuid import uuid4
from . import Base


class CreatedAt:
    createdAt = Column(DateTime, nullable=False, default="NOW()")


class UpdatedAt:
    updatedAt = Column(DateTime, nullable=False,
                       default="NOW()", onupdate="NOW()")


class TimeStamp(CreatedAt, UpdatedAt):
    pass


class User(Base, TimeStamp):
    __tablename__ = "user"
    id = Column(UUID, primary_key=True, nullable=False, default=uuid4)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(70), nullable=False)
    picture = Column(String(70), nullable=False, unique=True)


class Blog(Base, TimeStamp):
    __tablename__ = "blog"
    id = Column(UUID, primary_key=True, nullable=False, default=uuid4)
    title = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=False)
    bloggerId = Column(UUID, ForeignKey("user.id"), nullable=False)


class BlogImages(Base, CreatedAt):
    __tablename__ = "blogImages"
    id = Column(BigInteger, nullable=False, primary_key=True)
    image = Column(String(70), nullable=False)
    blogId = Column(UUID, ForeignKey("blog.id"), nullable=False)


class BlogLikes(Base, CreatedAt):
    __tablename__ = "blogLikes"
    id = Column(BigInteger, nullable=False, primary_key=True)
    blogId = Column(UUID, ForeignKey("blog.id"), nullable=False)
    likerId = Column(UUID, ForeignKey("user.id"), nullable=False)


class BlogComments(Base, TimeStamp):
    __tablename__ = "blogComments"
    id = Column(BigInteger, nullable=False, primary_key=True)
    comment = Column(String(255), nullable=False)
    blogId = Column(UUID, ForeignKey("blog.id"), nullable=False)
    commenterId = Column(UUID, ForeignKey("user.id"), nullable=False)
