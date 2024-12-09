from database import SessionLocal
from models import User

def add_users():
    session = SessionLocal()
    try:
        users = [
            User(username='john_doe', email='john@example.com', password='password123'),
            User(username='jane_smith', email='jane@example.com', password='securepass'),
            User(username='alice_jones', email='alice@example.com', password='alicepass')
        ]
        session.add_all(users)
        session.commit()
        print("Пользователи добавлены успешно.")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при добавлении пользователей: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    add_users()
