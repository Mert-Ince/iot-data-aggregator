from pydantic import BaseModel

class SensorBase(BaseModel):
    name: str
    type: str
    location: str | None = None
    unit: str

class SensorCreate(SensorBase):
    pass

class Sensor(SensorBase):
    id: int

    class Config:
        orm_mode = True
