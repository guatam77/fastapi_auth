from demo import *


class userschema(BaseModel) :
            id:int
            email:str    
            hashed_password :str
            is_active :bool 
            url : str
            
            
            class Config:
                orm_mode = True
                
                
          
class itemschema(BaseModel) :
            id:int
            title:str    
            description :str
            owner_id :int 
            
            class Config:
                orm_mode = True    
                                
                                
class loginschem(BaseModel):
    email : str 
    password : str   
       
    class Config:
        orm_mode = True                                 
        
        
class Token(BaseModel):
    access_token: str
    token_type: str
    class Config:
        orm_mode = True   

class TokenData(BaseModel):
    email: str   
    class Config:
        orm_mode = True   