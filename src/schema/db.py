from pydantic import BaseModel, UUID4, EmailStr


class User(BaseModel):
    id: UUID4
    username: str
    email: EmailStr
    password: str
    picture: str

    class Config:
        orm_mode = True


class Blog(BaseModel):
    id: UUID4
    title: str
    description: str
    bloggerId: UUID4

    class Config:
        orm_mode = True


class BlogImages(BaseModel):
    id: int
    image: str
    blogId: UUID4

    class Config:
        orm_mode = True


class BlogLikes(BaseModel):
    id: int
    blogId: UUID4
    likerId: UUID4

    class Config:
        orm_mode = True


class BlogComments(BaseModel):
    id: int
    comment: str
    blogId: UUID4
    commenterId: UUID4

    class Config:
        orm_mode = True
