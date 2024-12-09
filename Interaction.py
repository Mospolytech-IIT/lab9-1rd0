from sqlalchemy.orm import Session
from models import SessionLocal
from crud import create_user, create_post, get_users, get_posts, update_user_email, delete_post, delete_user

# Создаем сессию
db = SessionLocal()

# Создание пользователей
user1 = create_user(db, "john_doe", "john@example.com", "securepassword123")
user2 = create_user(db, "alice_smith", "alice@example.com", "anotherpassword123")

# Создание постов
post1 = create_post(db, "First Post", "This is the content of the first post", user1.id)
post2 = create_post(db, "Second Post", "This is the content of the second post", user2.id)

# Извлечение данных
users = get_users(db)
posts = get_posts(db)

# Обновление данных
update_user_email(db, user1.id, "new_email@example.com")

# Удаление данных
delete_post(db, post1.id)
delete_user(db, user1.id)

db.close()
