from utils.logging import logger
from fastapi import FastAPI
from schema import HouseInfo
import pandas as pd

# Creating FastAPI instance
app = FastAPI()

# Read offline data
dataset = pd.read_csv("train.csv")


# Creating an endpoint to receive the data
@app.get("/features", response_model=HouseInfo)
def predict(item_id: str):
    # Predicting the class
    logger.info("Get features...")

    # Get features for the requested item_id
    item_features = dataset[dataset.Id == int(item_id)]
    data = HouseInfo.model_validate(item_features.to_dict(orient="records")[0])

    return data
