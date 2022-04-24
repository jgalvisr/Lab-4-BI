from fastapi import FastAPI
import pandas as pd
from XDataModel import XDataModel
from YDataModel import YDataModel
from PredictionModel import Model

app = FastAPI()


@app.post("/predict")
def make_predictions(data_model: XDataModel):
    df = pd.DataFrame(data_model.dict(), columns=data_model.dict().keys(), index=[0])
    model = Model(data_model.columns())
    result = model.make_predictions(df)
    return "Life expectancy: " + str(result[0]) + " years"


@app.post("/test")
def test_r2(data_model: list[YDataModel]):
    data = []
    for i in range(len(data_model)):
        data.append(data_model[i].dict())
    df = pd.json_normalize(data)
    model = Model(data_model[0].columns())
    y = df['life_expectancy']
    x = df.drop(['life_expectancy'], axis=1)
    result = model.calculate_r2(x, y)
    return "R^2: " + str(result)

