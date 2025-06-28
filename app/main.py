from fastapi import FastAPI
from .core.middleware import LogRequestsMiddleware
from .routers import sensors

app = FastAPI(
    title="IoT Data Aggregator",
    version="0.1.0",
)

# Register custom middleware (e.g., request-logging)
app.add_middleware(LogRequestsMiddleware)

# Include the sensor “controller”
app.include_router(sensors.router)

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

app = FastAPI(
    title="IoT Data Aggregator",
    version="0.1.0",
)

app.include_router(sensors.router)
