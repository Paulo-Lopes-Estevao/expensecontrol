from sqlalchemy import Column, DateTime, Integer, String, Float,Enum
from sqlalchemy.orm import Session
import schema
from sqlalchemy.sql import func
from config.database import Base


class Spent(Base):
    __tablename__ = 'spent'
    id  = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    date = Column(DateTime(timezone=True), server_default=func.now())
    reason = Column(String)
    priority = Column(Enum('Alta', 'Media', 'Baixa', name='priority'))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    def SpentCreate(db: Session, spent: schema.Spent):
        priority = spent.priority.capitalize()
        db_spent = Spent(amount=spent.amount, reason=spent.reason, priority=priority)
        db.add(db_spent)
        db.commit()
        db.refresh(db_spent)
        return db_spent
