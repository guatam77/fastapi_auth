# https://www.youtube.com/watch?v=ijiVby4g4oI
from fastapi import Depends, FastAPI, File ,Form, UploadFile, Request,APIRouter
from pydantic import BaseModel, Json
from sqlalchemy import Column,String,Integer,Boolean, ForeignKey
from dbform import Base, engine , SessionLocal
from sqlalchemy.orm import Session,relationship
from pathlib import Path
import shutil
from routers import  user_logic , items ,authentications
from  typing import List, Optional
from passlib.context import CryptContext

from sqlalchemy_utils import URLType
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse




class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    img = Column(String, index=True)
    
    url = Column(String)
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






app.include_router(user_logic.router)           


app.include_router(items.router)     


app.include_router(authentications.router) 




     
                
                
# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)


# def get_password_hash(password):
#     return pwd_context.hash(password)



# @app.post('/img')
# def filedata(files:List[UploadFile] = File(...)):
#     for img in files:
#         with open(f'{img.filename}' , 'wb')as abc:
#             shutil.copyfileobj(img.file, abc)
    
#     return {'file name':"good"}                    
            


# def gert_db():
#     db = SessionLocal()
#     try:
#         yield db 
#     finally:
#         db.close()    
                
        
# class userschema(BaseModel) :
#             id:int
#             email:str    
#             hashed_password :str
#             is_active :bool 
#             url : str
            
            
#             class Config:
#                 orm_mode = True
                
                
# class itemschema(BaseModel) :
#             id:int
#             title:str    
#             description :str
#             owner_id :int 
            
#             class Config:
#                 orm_mode = True    
                
                            
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
                    
                    




            
            
# @app.post('/userform',response_model = userschema)
# async def userform(usr:userschema,db:Session=Depends(gert_db)):
#     hashpass = pwd_context.hash(usr.hashed_password)
#     tform = User(id =usr.id,email=usr.email, hashed_password = hashpass, is_active = usr.is_active, url=usr.url)
#     db.add(tform)
#     db.commit()
#     return tform         
   


# @app.post('/itmform',response_model = itemschema)
# async def userform(itm:itemschema ,db:Session=Depends(gert_db)):
#     iform = Item(id =itm.id ,title=itm.title, description = itm.description, owner_id = itm.owner_id)
#     db.add(iform)
#     db.commit()
#     return iform            


# @app.get('/data', response_model= List[userschema])
# async def userdata(request:Request,db:Session=Depends(gert_db)):
#     u = db.query(User).all()
#     print(u)
#     return u


# @app.get('/idata', response_model= List[itemschema])
# async def itemdata(request:Request,db:Session=Depends(gert_db)):
#     u = db.query(Item).all()
#     print(u)
#     return u




# @app.put('/upuser/<int:id>',response_model = userschema)
# async def userup(id:int, i:userschema, db:Session=Depends(gert_db)):
#     user = db.query(User).get(id)
#     user.email = i.email
#     user.is_active = i.is_active
#     db.commit()
#     print(user.email)
#     print(user.is_active)
#     return user




# @app.delete('/deluser/<int:id>',response_model=userschema)
# async def userdelete(id:int, db:Session=Depends(gert_db)):
#     user = db.query(User).get(id)
#     db.delete(user)
#     db.commit()
#     return user








