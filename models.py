from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Text
from werkzeug.security import generate_password_hash, check_password_hash


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class City(db.Model):
    __tablename__ = 'cities'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    temp_now: Mapped[float] = mapped_column(Float)
    humidity: Mapped[int] = mapped_column(Integer)
    wind_speed: Mapped[float] = mapped_column(Float)
    pressure: Mapped[int] = mapped_column(Integer)

    def to_dict(self):
        """Вывод данных в виде словаря"""

        return {
            "id": self.id,
            "name": self.name,
            "temp_now": self.temp_now,
            "humidity": self.humidity,
            "wind_speed": self.wind_speed,
            "pressure": self.pressure,
        }


class Users(db.Model):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(Text, nullable=False)

    def set_password(self, password):
        """Сохраняем Хэшированный пароль"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Проверка пароля"""
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Вывод данных в виде словаря"""

        return {"id": self.id,
                "username": self.username,
                }
