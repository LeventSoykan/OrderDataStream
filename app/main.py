from fastapi import FastAPI, BackgroundTasks
import random
import string
import time
import threading
import uvicorn
from data_generator import create_order_set

app = FastAPI()

orders = []

def generate_orders():
    global orders
    while True:
        orders = create_order_set()
        interval = random.choice([60, 180, 300])  # Random interval of 1 min, 3 min, or 5 min
        time.sleep(interval)

threading.Thread(target=generate_orders, daemon=True).start()

@app.get("/random_orders")
def get_random_orders():
    return {"random_orders": orders}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)