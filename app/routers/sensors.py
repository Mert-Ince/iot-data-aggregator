from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/sensors",
    tags=["sensors"],
)

@router.post("/", response_model=schemas.Sensor, status_code=status.HTTP_201_CREATED)
def create_sensor(sensor_in: schemas.SensorCreate, db: Session = Depends(get_db)):
    # 1. Instantiate the model
    db_sensor = models.Sensor(**sensor_in.dict())
    # 2. Add & commit to DB
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)      # loads the new id
    # 3. Return the created object
    return db_sensor
