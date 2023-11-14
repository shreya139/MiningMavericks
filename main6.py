from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI
from CricketDataModel import CricketMatch
import pickle
import pandas as pd

app = FastAPI()

# Load the RandomForestClassifier model
with open("classifier.pkl", "rb") as pickle_model:
    classifier = pickle.load(pickle_model)

# Load the ColumnTransformer used for preprocessing

file_path_ct = "column_transformer.pkl"
try:
    with open(file_path_ct, "rb") as pickle_model_ct:
        ct = pickle.load(pickle_model_ct)
except FileNotFoundError:
    print(f"Error: File '{file_path_ct}' not found.")
except EOFError:
    print(f"Error: Ran out of input while loading '{file_path_ct}'.")
except Exception as e:
    print(f"Error: {e}")


@app.post("/predict")
def predict(data: CricketMatch):
    # Extract features
    features = [
        data.wides,
        data.noballs,
        data.byes,
        data.legbyes,
        data.penalty,
        data.balls_left,
        data.cumulative_runs,
        data.run_rate,
        data.target_runs,
        data.req_runs,
        data.req_rr
    ]

    # Convert the list of features to a DataFrame for preprocessing
    features_df = pd.DataFrame([features])

    # Apply the same preprocessing used during training
    features_transformed = column_transformer.transform(features_df)

    # Make prediction
    prediction = classifier.predict(features_transformed)

    # Return prediction
    if prediction[0] > 0.5:
        prediction_label = "Wicket"
    else:
        prediction_label = "No wicket"

    return {
        'prediction': prediction_label
    }

# Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
