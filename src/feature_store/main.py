from utils.logging import logger
from fastapi import FastAPI
from schema import HouseInfo
import pandas as pd
import redis
import json
import os

# Creating FastAPI instance
app = FastAPI()

# Connect to Redis (assuming host 'redis-master')
REDIS_HOST = os.environ.get("REDIS_HOST", "redis-master")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))

try:
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    
    # Read offline data and populate Redis on startup if it's empty
    # In production, this would be done by a separate data-loading job
    dataset = pd.read_csv("train.csv")
    if not r.exists("house:1"):
        logger.info("Redis is empty. Populating data from train.csv...")
        records = dataset.to_dict(orient="records")
        for row in records:
            r.set(f"house:{row['Id']}", json.dumps(row))
        logger.info("Successfully populated Redis with train.csv data.")
except Exception as e:
    logger.error(f"Could not connect to Redis during startup: {e}")
    r = None
    dataset = pd.read_csv("train.csv")


# Creating an endpoint to receive the data
@app.get("/features", response_model=HouseInfo)
def get_features(item_id: str):
    logger.info(f"Get features for item {item_id}...")
    
    if r:
        try:
            cached_data = r.get(f"house:{item_id}")
            if cached_data:
                logger.info("Cache HIT! Returning from Redis.")
                data = HouseInfo.model_validate(json.loads(cached_data))
                return data
            else:
                logger.info("Cache MISS!")
        except Exception as e:
            logger.error(f"Redis error: {e}")
            
    # Fallback to in-memory pandas dataframe
    logger.info("Fallback: Reading from Pandas memory...")
    item_features = dataset[dataset.Id == int(item_id)]
    data = HouseInfo.model_validate(item_features.to_dict(orient="records")[0])
    return data
