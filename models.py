from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker
 
# Определение базы данных
Base = declarative_base()

# Модель для Users
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    posts = relationship('Post', back_populates='owner')  # Связь с таблицей Posts

# Модель для Posts
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='posts')  # Обратная связь с таблицей Users

 