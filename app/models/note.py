from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, Text, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base_class import Base

# Связующая таблица для тегов и заметок
note_tags = Table(
    'note_tags',
    Base.metadata,
    Column('note_id', Integer, ForeignKey('notes.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Связь many-to-many с заметками
    notes = relationship("Note", secondary=note_tags, back_populates="tags")

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    is_public = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Внешний ключ для связи с пользователем
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="notes")

    # Связь many-to-many с тегами
    tags = relationship("Tag", secondary=note_tags, back_populates="notes")
