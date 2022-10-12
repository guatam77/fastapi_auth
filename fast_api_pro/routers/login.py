# from demo import *





# def gert_db():
#     db = SessionLocal()
#     try:
#         yield db 
#     finally:
#         db.close() 




# router = APIRouter()

# @router.post('/login')
# def login(request:userschema , db:Session=Depends(gert_db)):
#     user = db.query(User).filter(request.email).first()
#     return user