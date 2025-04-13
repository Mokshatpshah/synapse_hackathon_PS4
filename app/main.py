from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("models/inference_pipeline.pkl")

class UserBehavior(BaseModel):
    age_group: str
    tech_savviness: str
    interests: str
    device: str
    action: str
    items_added_to_cart: int
    affluence_score: int

@app.post("/predict/")
def predict_traits(data: UserBehavior):
    input_df = pd.DataFrame([data.dict()])
    predictions = model.predict(input_df)
    return {
        "affluence_level": predictions[0][0],
        "consumer_trait": predictions[0][1]
    }
