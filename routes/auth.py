from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import User, Ticket, UserModel
from database import engine, SessionLocal
from passlib.context import CryptContext
 

 

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_password_hash(password):
    return pwd_context.hash(password)

# User signup
@router.post("/signup")
async def signup(user: User, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    db_user = UserModel(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    return {"message": f"User {user.username} created successfully"}

# User login
@router.post("/login")
async def login(user: User, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    if not db_user or not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": f"Welcome {user.username}!"}