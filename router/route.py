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


@router.get("/spent")
async def home(db: Session = Depends(get_db)):
    return EntitySpent.SpentGetAll(db)

@router.post("/spent", response_model=SchemaSpent)
async def spent_create(spent: SchemaSpent, db: Session = Depends(get_db)):
    try:
        return await EntitySpent.SpentCreate(db, spent)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/spent/{reason}")
async def spent_list(reason: str, db : Session = Depends(get_db)):
    try:
        return await EntitySpent.SpentGetReason(db,reason)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(f"not found {e}"))

@router.put("/spent/{id}")
async def spent_update(spent: SchemaSpent, id: str, db : Session = Depends(get_db)):
    try:
        return EntitySpent.SpentUpdate(spent, id, db)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(f"not found {e}"))

@router.delete("/spent/{id}")
async def spent_delete(id: str, db: Session =Depends(get_db)):
    try:
        return EntitySpent.SpentDelete(id, db)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(f"not found {e}"))