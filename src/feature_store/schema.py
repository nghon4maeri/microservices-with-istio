from pydantic import BaseModel


# Type hint for attributes of a house
class HouseInfo(BaseModel):
    MSSubClass: int = 60
    MSZoning: str = "RL"
    LotArea: int = 7844
    Street: str = "Pave"
    LotShape: str = "Reg"
    LandContour: str = "Lvl"
    Utilities: str = "AllPub"
    LotConfig: str = "Inside"
    LandSlope: str = "Gtl"
    Neighborhood: str = "Sawyer"
    Condition1: str = "Norm"
    Condition2: str = "Norm"
    BldgType: str = "1Fam"
    HouseStyle: str = "2Story"
    OverallQual: int = 6
    OverallCond: int = 7
    YearBuilt: int = 1978
    YearRemodAdd: int = 1978
    RoofStyle: str = "Hip"
    RoofMatl: str = "CompShg"
    Exterior1st: str = "HdBoard"
    Exterior2nd: str = "HdBoard"
    ExterQual: str = "TA"
    ExterCond: str = "TA"
    Foundation: str = "CBlock"
    BsmtFinSF1: int = 209
    BsmtFinSF2: int = 0
    BsmtUnfSF: int = 463
    TotalBsmtSF: int = 672
    Heating: str = "GasA"
    HeatingQC: str = "TA"
    CentralAir: str = "Y"
    LowQualFinSF: int = 0
    GrLivArea: int = 1400
    BsmtFullBath: int = 0
    BsmtHalfBath: int = 0
    FullBath: int = 1
    HalfBath: int = 1
    BedroomAbvGr: int = 3
    KitchenAbvGr: int = 1
    KitchenQual: str = "TA"
    TotRmsAbvGrd: int = 6
    Functional: str = "Typ"
    Fireplaces: int = 1
    GarageCars: int = 2
    GarageArea: int = 440
    PavedDrive: str = "Y"
    WoodDeckSF: int = 0
    OpenPorchSF: int = 0
    EnclosedPorch: int = 0
    ScreenPorch: int = 0
    PoolArea: int = 0
    MiscVal: int = 0
    MoSold: int = 3
    YrSold: int = 2006
    SaleType: str = "WD"
    SaleCondition: str = "Normal"


# Type hint for all the predictions of a house
class HousePrediction(BaseModel):
    Price: float
