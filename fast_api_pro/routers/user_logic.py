
from fastapi import APIRouter

import demo
import schemas
from passlib.context import CryptContext
from fastapi import Depends
from sqlalchemy.orm import Session,relationship
from  typing import List, Optional
from dbform import Base, engine , SessionLocal
router = APIRouter()

import oauth2

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
                    
                    



def gert_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()    




@router.get('/data', response_model= List[schemas.userschema],tags=["user"])
async def userdata(db:Session = Depends(gert_db),get_current_user:schemas.userschema  = Depends(oauth2.get_current_user)):
    u = db.query(demo.User).all()
    print(u)
    return u

@router.post('/userform',response_model = schemas.userschema, tags=["user"])
async def userform(usr:schemas.userschema,db:Session=Depends(gert_db)):
    hashpass = pwd_context.hash(usr.hashed_password)
    tform = demo.User(id =usr.id,email=usr.email, hashed_password = hashpass, is_active = usr.is_active, url=usr.url)
    db.add(tform)
    db.commit()
    return tform         
                       
@router.put('/upuser/<int:id>',response_model = schemas.userschema,tags=["user"])
async def userup(id:int, i:schemas.userschema, db:Session=Depends(gert_db)):
    user = db.query(demo.User).get(id)
    user.email = i.email
    user.is_active = i.is_active
    db.commit()
    print(user.email)
    print(user.is_active)
    return user




@router.delete('/deluser/<int:id>',response_model=schemas.userschema,tags=["user"])
async def userdelete(id:int, db:Session=Depends(gert_db)):
    user = db.query(demo.User).get(id)
    db.delete(user)
    db.commit()
    return user
