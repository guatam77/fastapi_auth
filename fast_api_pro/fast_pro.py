

from fastapi import Depends, FastAPI, File ,Form, UploadFile, Request
from  typing import List, Optional
from pydantic import BaseModel, Json
from sqlalchemy import Column,String,Integer,Boolean, ForeignKey
from fastapi.responses import HTMLResponse
from dbform import Base, engine , SessionLocal
from sqlalchemy.orm import Session,relationship
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="htmlfile")



class Teacher(Base):
        __tablename__ = 'Teacher'
        id = Column(Integer, primary_key=True)         
        name  = Column(String,nullable=False)
        school = Column(String,nullable=False)
        img  = Column(String , nullable=False) 
        demo1 = relationship("Student", back_populates='teacher')
        

class Student(Base):
        __tablename__ = 'Student'
        id = Column(Integer, primary_key=True)
        name  = Column(String,nullable=False)
        std  = Column(String,nullable=False)
        result = Column(String,nullable=False)
        img  = Column( String, nullable=False)  
        teaid = Column(Integer, ForeignKey('Teacher.id'))  
        demo2 = relationship("Teacher", back_populates='students')



Base.metadata.create_all(bind=engine)   
app = FastAPI()


def gert_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()


class studentschema(BaseModel):
    id : int
    name : str
    result : str
    img : str 
    std : str
    teaid : int 
    class Config:
        orm_mode = True

class teacherschema(BaseModel):
    id:int
    name:str 
    school:str
    img:str 
    
    class Config:
        orm_mode = True
                                                                                                                                      



@app.post('/teaform/',response_model = teacherschema)
def teacherform(tea:teacherschema ,db:Session=Depends(gert_db)):
    tform = Teacher(id =tea.id ,name=tea.name, school = tea.school, img = tea.img)
    db.add(tform)
    db.commit()
    return tform




# if __name__ == '__main__':

#  uvicorn.run(app, host="127.0.0.1", port=5000)







