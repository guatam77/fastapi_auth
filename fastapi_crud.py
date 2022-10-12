
# https://www.youtube.com/watch?v=ijiVby4g4oI
from fastapi import Depends, FastAPI, File ,Form, UploadFile, Request
from  typing import List, Optional
from pydantic import BaseModel, Json
from sqlalchemy import Column,String,Integer,Boolean, ForeignKey
from fastapi.responses import HTMLResponse
from dbform import Base, engine , SessionLocal
from sqlalchemy.orm import Session,relationship
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates






class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    img = Column(String, index=True)
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
  
    owner = relationship("User", back_populates="items")
    
    
Base.metadata.create_all(bind=engine)   
app = FastAPI()


def gert_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()    
        
        
        
class userschema(BaseModel) :
            id:int
            email:str    
            hashed_password :str
            is_active :bool 
            
            
            class Config:
                orm_mode = True
                
class itemschema(BaseModel) :
            id:int
            title:str    
            description :str
            owner_id :int 
            
            class Config:
                orm_mode = True                
                
                
                
            
@app.post('/userform',response_model = userschema)
def userform(usr:userschema ,db:Session=Depends(gert_db)):
    tform = User(id =usr.id ,email=usr.email, hashed_password = usr.hashed_password, is_active = usr.is_active)
    db.add(tform)
    db.commit()
    return tform            


@app.post('/itmform',response_model = itemschema)
async def userform(itm:itemschema ,db:Session=Depends(gert_db)):
    iform = Item(id =itm.id ,title=itm.title, description = itm.description, owner_id = itm.owner_id)
    db.add(iform)
    db.commit()
    return iform            


@app.get('/data', response_model= List[userschema])
async def userdata(request:Request,db:Session=Depends(gert_db)):
    u = db.query(User).all()
    print(u)
    return u


@app.get('/idata', response_model= List[itemschema])
async def itemdata(request:Request,db:Session=Depends(gert_db)):
    u = db.query(Item).all()
    print(u)
    return u




@app.put('/upuser/<int:id>',response_model = userschema)
async def userup(id:int, i:userschema, db:Session=Depends(gert_db)):
    user = db.query(User).get(id)
    user.email = i.email
    user.is_active = i.is_active
    db.commit()
    print(user.email)
    print(user.is_active)
    return user




@app.delete('/deluser/<int:id>',response_model=userschema)
async def userdelete(id:int, db:Session=Depends(gert_db)):
    user = db.query(User).get(id)
    db.delete(user)
    db.commit()
    return user








