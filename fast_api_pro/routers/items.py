from fastapi import APIRouter
import oauth2
import demo
import schemas
from passlib.context import CryptContext
from fastapi import Depends
from sqlalchemy.orm import Session,relationship
from  typing import List, Optional
from dbform import Base, engine , SessionLocal
router = APIRouter()



def gert_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()    
        
        
@router.post('/itmform',response_model = schemas.itemschema, tags=["items"])
async def userform(itm:schemas.itemschema ,db:Session=Depends(gert_db)):
    iform = demo.Item(id =itm.id ,title=itm.title, description = itm.description, owner_id = itm.owner_id)
    db.add(iform)
    db.commit()
    return iform              



@router.get('/idata', response_model= List[schemas.itemschema],tags=["items"])
async def itemdata(db:Session=Depends(gert_db),get_current_user:schemas.itemschema=Depends(oauth2.get_current_user)):
    u = db.query(demo.Item).all()
    print(u)
    return u






