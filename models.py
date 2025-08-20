from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


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
