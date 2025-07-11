from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator
import time
import random

app = FastAPI()
instrumentator = Instrumentator().instrument(app).expose(app)

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

@app.get("/fast")
def fast_response():
    time.sleep(0.1)  # 100ms delay
    return {"message": "Fast response"}

@app.get("/slow")
def slow_response():
    time.sleep(1.5)  # 1500ms delay
    return {"message": "Slow response"}

@app.post("/submit")
def submit_data():
    time.sleep(0.3)  # Simulate some processing
    return {"message": "Data submitted"}

@app.put("/update")
def update_data():
    time.sleep(0.5)
    return {"message": "Data updated"}

@app.get("/random-latency")
def random_latency():
    delay = random.uniform(0, 2)
    time.sleep(delay)
    return {"message": f"Random delay of {delay:.2f} seconds"}

@app.get("/error")
def return_error():
    raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/bad-request")
def bad_request():
    raise HTTPException(status_code=400, detail="Bad request")

@app.get("/metrics-check")
def health_check():
    return {"status": "ok"}
