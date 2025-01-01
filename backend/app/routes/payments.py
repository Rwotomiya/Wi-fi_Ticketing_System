from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()

PAYMENT_GATEWAY_URL = "https://your-payment-gateway-endpoint"

@router.post("/process-payment")
async def process_payment(ticket_id: int, user_id: int):
    payload = {"ticket_id": ticket_id, "user_id": user_id, "amount": 10.0}  # Adjust as needed
    response = requests.post(PAYMENT_GATEWAY_URL, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Payment failed")
    return {"message": "Payment successful"}
