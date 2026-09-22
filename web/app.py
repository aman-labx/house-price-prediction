from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "src",
    "house_price_model.pkl"
)

model = joblib.load(MODEL_PATH)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        input_data = pd.DataFrame([{
            "house_size_sqft": float(data["house_size_sqft"]),
            "bedrooms": int(data["bedrooms"]),
            "bathrooms": int(data["bathrooms"]),
            "age_years": int(data["age_years"]),
            "distance_to_city_km": float(data["distance_to_city_km"]),
            "parking_spaces": int(data["parking_spaces"])
        }])

        prediction = model.predict(input_data)[0]

        return jsonify({
            "success": True,
            "predicted_price": round(float(prediction), 2)
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)