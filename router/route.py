from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db
from schema import Spent as SchemaSpent
from config.database import engine, SessionLocal
from entity.spending import Spent  as EntitySpent
from sqlalchemy.orm import Session

EntitySpent.metadata.create_all(bind=engine)

router = APIRouter(
    prefix='/api',
    tags=['Spending'],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.post("/spent", response_model=SchemaSpent)
async def spent_create(spent: SchemaSpent, db: Session = Depends(get_db)):
    try:
        return EntitySpent.SpentCreate(db, spent)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/spent", response_model=SchemaSpent)
async def spent_list():
    db_sent = db.session.query(EntitySpent).all()
    return db_sent