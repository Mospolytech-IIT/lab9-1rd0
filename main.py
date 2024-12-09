from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import SessionLocal, create_user, create_post, get_users, get_posts, update_user_email, delete_post, delete_user
from pydantic import BaseModel

# Инициализация FastAPI
app = FastAPI()

# Модели Pydantic для входных данных
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int

# Зависимость для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Роут для добавления пользователя
@app.post("/users/")
def create_user_view(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.username, user.email, user.password)

# Роут для добавления поста
@app.post("/posts/")
def create_post_view(post: PostCreate, db: Session = Depends(get_db)):
    return create_post(db, post.title, post.content, post.user_id)

# Роут для получения всех пользователей
@app.get("/users/")
def get_users_view(db: Session = Depends(get_db)):
    return get_users(db)

# Роут для получения всех постов
@app.get("/posts/")
def get_posts_view(db: Session = Depends(get_db)):
    return get_posts(db)

# Роут для обновления email пользователя
@app.put("/users/{user_id}")
def update_email(user_id: int, email: str, db: Session = Depends(get_db)):
    return update_user_email(db, user_id, email)

# Роут для удаления поста
@app.delete("/posts/{post_id}")
def delete_post_view(post_id: int, db: Session = Depends(get_db)):
    return delete_post(db, post_id)

# Роут для удаления пользователя
@app.delete("/users/{user_id}")
def delete_user_view(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)
