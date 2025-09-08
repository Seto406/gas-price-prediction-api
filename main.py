from fastapi import FastAPI
import joblib

# Create a FastAPI application instance
app = FastAPI(title="Gas Price Prediction API")

# --- 1. Load the model ---
# Load the trained model from the file
model = joblib.load('gas_price_predictor.joblib')

print("Model loaded successfully.")


# --- 2. Define the prediction endpoint ---
# This tells FastAPI that this function will handle requests to your API
@app.post("/predict")
def predict_price(previous_week_price: float):
    """
    Takes a previous week's price and returns a prediction.
    """
    # Prepare the input for the model
    # (It expects a 2D array, so we wrap it in a list of a list)
    input_data = [[previous_week_price]]

    # Use the loaded model to make a prediction
    prediction = model.predict(input_data)

    # Return the prediction in a JSON response
    return {"predicted_price": prediction[0]}


# --- 3. Define a root endpoint for health checks ---
@app.get("/")
def read_root():
    return {"status": "API is running."}