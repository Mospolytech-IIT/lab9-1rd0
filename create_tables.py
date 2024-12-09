# create_tables.py
from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import sessionmaker

 
# Параметры подключения к PostgreSQL
DATABASE_URL = "postgresql+psycopg2://postgres:2550@localhost:5432/lab9"
 
# Создание движка для подключения

engine = create_engine(DATABASE_URL)
# Создание сессии

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание всех таблиц
Base.metadata.create_all(engine)

print("Таблицы успешно созданы.")
