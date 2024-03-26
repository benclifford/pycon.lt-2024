import dataclasses
import sqlalchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Score(Base):
    __tablename__ = "scores"
    name: Mapped[str] = mapped_column(primary_key=True)
    score: Mapped[int]


high_scores = [Score(name="Sally", score=107),
               Score(name="Ben", score=99),
               Score(name="Philip", score=78)]


engine = sqlalchemy.create_engine("sqlite:///./scores.sql", echo=True)
Base.metadata.create_all(engine)    

with Session(engine) as session:
    session.add_all(high_scores)
    session.commit()
