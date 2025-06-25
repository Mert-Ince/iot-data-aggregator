from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import get_db

app = FastAPI(
    title="IoT Data Aggregator",
    version="0.1.0",
    description="A demo API for sensor data aggregation"
)

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    """
    Simple Hello endpoint.
    Shows DI (`Depends`) for a DB session—even if unused here.
    """
    # you could verify connection: db.execute("SELECT 1")
    return {"message": "Hello, world!"}
