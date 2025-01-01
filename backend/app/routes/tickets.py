from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from models import Ticket, TicketModel
from database import engine, SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Add a ticket
@router.post("/add-ticket")
async def add_ticket(ticket: Ticket, db: Session = Depends(get_db)):
    db_ticket = TicketModel(ticket_type=ticket.ticket_type, price=ticket.price, duration=ticket.duration)
    db.add(db_ticket)
    db.commit()
    return {"message": "Ticket added successfully"}

# Purchase a ticket
@router.post("/purchase-ticket")
async def purchase_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(TicketModel).filter(TicketModel.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"message": f"Ticket {ticket.ticket_type} purchased successfully"}