from sqlalchemy.orm import declarative_base

from sqlalchemy import Column, Integer, String, Float,ForeignKey

Base = declarative_base()


# Without Base:
# class User:
# is just a Python class.

# With Base:
# class User(Base):
# SQLAlchemy understands:
# This class = database table
class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True   #index=True, Creates database index, Makes searching faster.
    )
    
    name = Column(
        String,
        nullable=False
    )


    email = Column(
        String,
        unique=True,
        nullable=False
    )

    password_hash = Column(
        String,
        nullable=False
    )


class Analysis(Base):

    __tablename__ = "analyses"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    idea = Column(
        String,
        nullable=False
    )

    score = Column(
        Float
    )