import datetime

from sqlalchemy import Column, DateTime, Integer, String, Float,Enum, extract, and_, func
from sqlalchemy.orm import Session
import schema
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

    def SpentGetAll(db: Session):
        db_spent = db.query(Spent).all()
        return db_spent

    def SpentGetReason(db: Session, reason: str):
        db_spent = db.query(func.avg(Spent.amount).label('average_spent_per_month')).filter(and_(extract('month',Spent.date) == datetime.datetime.now().month, (Spent.reason == reason)))
        return db_spent[0]



    def SpentUpdate(spent: schema.Spent, id: str, db: Session):
        db_spent = db.query(Spent).filter(Spent.id == id)
        data = verifyValueSpent(**spent.dict())

        db_spent.all()[0].amount = data.get("amount",None)
        db_spent.all()[0].reason = data.get("reason",)
        db_spent.all()[0].priority = data.get("priority",None)
        db.commit()
        return "dados atualizado"

    def SpentDelete(id, db: Session):
        db.query(Spent).filter(Spent.id == id).delete()
        db.commit()
        return "dados apagados"


def verifyValueSpent(**kwargs):
    result = {k: v for k, v in kwargs.items() if v != "string"}
    return result