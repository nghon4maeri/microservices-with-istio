import os

import joblib
from fastapi import FastAPI
from schema import HousePrediction
from utils.data_processing import format_input_data
from utils.logging import logger
from opentelemetry import metrics
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.metrics import set_meter_provider
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from prometheus_client import start_http_server
from fastapi import Header
from typing import Optional
import random
import requests

# Start Prometheus client
start_http_server(port=8099, addr="0.0.0.0")

# Service name is required for most backends
resource = Resource(attributes={SERVICE_NAME: "house-price-service"})

# Exporter to export metrics to Prometheus
reader = PrometheusMetricReader()

# Meter is responsible for creating and recording metrics
provider = MeterProvider(resource=resource, metric_readers=[reader])
set_meter_provider(provider)
meter = metrics.get_meter("house-price", "0.0.1")


counter = meter.create_counter(
    name="house_price_random_like_counter",
    description="House price prediction random like counter",
)

# Creating FastAPI instance
app = FastAPI()
# Loading model with default path models/model.pkl
clf = joblib.load(os.environ.get("MODEL_PATH", "/app/model.pkl"))


# Creating an endpoint to receive the data
# to make prediction on
@app.post("/predict", response_model=HousePrediction)
def predict(item_id: str, x_user_group: Optional[str] = Header(None)):
    # Predicting the class
    logger.info("Make predictions...")

    data = requests.get(
        "http://feature-store.default.svc.cluster.local/features?item_id=1"
    ).json()
    # Convert data to pandas DataFrame and make predictions
    price = clf.predict(format_input_data(data))[0]

    label = {
        "api": "/predict",
        "user_group": x_user_group if x_user_group else "unknown",
    }
    is_like = random.choices([0, 1], weights=(50, 50))[0]
    if is_like:
        counter.add(is_like, label)

    # Return the result
    return HousePrediction(Price=price)
