from fastapi import APIRouter ,HTTPException ,status
import demo
import schemas
from passlib.context import CryptContext
from fastapi import Depends
from sqlalchemy.orm import Session,relationship
from  typing import List, Optional
from dbform import Base, engine , SessionLocal
from datetime import datetime, timedelta
import tokens
from fastapi.security import OAuth2PasswordBearer ,OAuth2PasswordRequestForm

router = APIRouter()

# from hashing import Hash

def gert_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()    
        



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
                    
                 

def verify_password(hashed_password,plain_password,):
        return pwd_context.verify(hashed_password,plain_password)
    
    
    


@router.post('/login',tags=["auth"])
def login(auth:OAuth2PasswordRequestForm = Depends(),db:Session=Depends(gert_db)):
    
    user = db.query(demo.User).filter(demo.User.email == auth.username).first() 
    
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,   detail = f"invalid crediantioal")
    
    # if not verify_password(demo.User.hashed_password , auth.password):
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,   detail = f"invalid crediantioal")
    
    
    access_token =  tokens.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}




