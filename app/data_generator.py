
import pandas as pd
import random
from datetime import datetime, timedelta

stores = [i for i in range(1000, 1051)]

products = pd.read_csv('./data/product_list.csv', header=0)
              
num_orders = random.randint(1,11)

def create_random_timestamp():
    now = datetime.now()
    random_seconds = random.randint(0, 300)
    return now - timedelta(seconds=random_seconds)

orders = []
for _ in range(num_orders):
    idx = random.randint(1,30)
    product_id = int((products.iloc[idx, 0] ))
    product = products.iloc[idx, 1]
    price = float(products.iloc[idx, 2])
    store_id = random.choice(stores)
    timestamp = create_random_timestamp()
    orders.append([timestamp, product_id, product, price, store_id])

print(orders)





