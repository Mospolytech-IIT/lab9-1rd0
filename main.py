from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from create_tables import SessionLocal
from models import User, Post
from pydantic import BaseModel
from sqlalchemy.exc import SQLAlchemyError

app = FastAPI()

# Dependency для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic модели для валидации данных
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class PostCreate(BaseModel):
    title: str
    content: str

# CRUD операции

# Создание пользователя
@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Получение всех пользователей
@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# Получение конкретного пользователя по ID
@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Обновление пользователя
@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_user.username = user.username
    db_user.email = user.email
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user

# Удаление пользователя
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}

# Создание поста
@app.post("/posts/")
def create_post(user_ids:int,post: PostCreate, db: Session = Depends(get_db)):
    db_post = Post(title=post.title, content=post.content, user_id=user_ids)  # Можно добавить реальную логику для привязки к пользователю
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# Получение всех постов
@app.get("/posts/")
def get_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()

# Получение конкретного поста по ID
@app.get("/posts/{post_id}")
def get_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

# Обновление поста
@app.put("/posts/{post_id}")
def update_post(post_id: int, post: PostCreate, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    
    db_post.title = post.title
    db_post.content = post.content
    db.commit()
    db.refresh(db_post)
    return db_post

# Удаление поста
@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    
    db.delete(db_post)
    db.commit()
    return {"message": "Post deleted successfully"}
