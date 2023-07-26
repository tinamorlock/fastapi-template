from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

# these are the DB models for SQL Alchemy.
# if these are not set up when the app starts, it will automatically create them in postgres.

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    bio = Column(String, nullable=True)
    website = Column(String, nullable=True)
    facebook_link = Column(String, nullable=True)
    twitter_link = Column(String, nullable=True)
    ig_link = Column(String, nullable=True)
    tiktok_link = Column(String, nullable=True)
    amazon_link = Column(String, nullable=True)
    goodreads_link = Column(String, nullable=True)
    bookbub_link = Column(String, nullable=True)
    is_author = Column(Boolean, nullable=False, server_default='False')
    genre = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))