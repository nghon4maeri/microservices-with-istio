import random
from locust import HttpUser, task, between

# Example payload (you can make a list of different payloads if you want more variation)
BASE_PAYLOAD = {
    "MSSubClass": 60,
    "MSZoning": "RL",
    "LotArea": 7844,
    "Street": "Pave",
    "LotShape": "Reg",
    "LandContour": "Lvl",
    "Utilities": "AllPub",
    "LotConfig": "Inside",
    "LandSlope": "Gtl",
    "Neighborhood": "Sawyer",
    "Condition1": "Norm",
    "Condition2": "Norm",
    "BldgType": "1Fam",
    "HouseStyle": "2Story",
    "OverallQual": 6,
    "OverallCond": 7,
    "YearBuilt": 1978,
    "YearRemodAdd": 1978,
    "RoofStyle": "Hip",
    "RoofMatl": "CompShg",
    "Exterior1st": "HdBoard",
    "Exterior2nd": "HdBoard",
    "ExterQual": "TA",
    "ExterCond": "TA",
    "Foundation": "CBlock",
    "BsmtFinSF1": 209,
    "BsmtFinSF2": 0,
    "BsmtUnfSF": 463,
    "TotalBsmtSF": 672,
    "Heating": "GasA",
    "HeatingQC": "TA",
    "CentralAir": "Y",
    "LowQualFinSF": 0,
    "GrLivArea": 1400,
    "BsmtFullBath": 0,
    "BsmtHalfBath": 0,
    "FullBath": 1,
    "HalfBath": 1,
    "BedroomAbvGr": 3,
    "KitchenAbvGr": 1,
    "KitchenQual": "TA",
    "TotRmsAbvGrd": 6,
    "Functional": "Typ",
    "Fireplaces": 1,
    "GarageCars": 2,
    "GarageArea": 440,
    "PavedDrive": "Y",
    "WoodDeckSF": 0,
    "OpenPorchSF": 0,
    "EnclosedPorch": 0,
    "ScreenPorch": 0,
    "PoolArea": 0,
    "MiscVal": 0,
    "MoSold": 3,
    "YrSold": 2006,
    "SaleType": "WD",
    "SaleCondition": "Normal",
}


class PredictUser(HttpUser):
    wait_time = between(1, 3)  # Wait time between requests (1-3s)

    @task
    def send_predict(self):
        # Randomly pick user group
        group = random.choice(["A", "B"])

        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "x-user-group": group,
        }

        # Send POST request
        self.client.post("/predict", headers=headers, params={"item_id": "2"})
