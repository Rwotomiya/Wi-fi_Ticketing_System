from fastapi import FastAPI
from routes import auth, tickets




app = FastAPI()
# Include the routes
app.include_router(auth.router)
app.include_router(tickets.router)

@app.get("/")
def read_root():
    return {"message":"Welcome to the Ticketing System!"}
