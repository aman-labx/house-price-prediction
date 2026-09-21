import pandas as pd
import joblib
import os


# Load trained model
model_path = os.path.join(
    os.path.dirname(__file__),
    "house_price_model.pkl"
)

model = joblib.load(model_path)


def predict_price(
    house_size_sqft,
    bedrooms,
    bathrooms,
    age_years,
    distance_to_city_km,
    parking_spaces
):
    input_data = pd.DataFrame([{
        "house_size_sqft": house_size_sqft,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "age_years": age_years,
        "distance_to_city_km": distance_to_city_km,
        "parking_spaces": parking_spaces
    }])

    prediction = model.predict(input_data)

    return prediction[0]


if __name__ == "__main__":

    print("House Price Prediction")
    print("----------------------")

    house_size = float(input("Enter house size (sqft): "))
    bedrooms = int(input("Enter number of bedrooms: "))
    bathrooms = int(input("Enter number of bathrooms: "))
    age = int(input("Enter house age (years): "))
    distance = float(input("Enter distance to city (km): "))
    parking = int(input("Enter parking spaces: "))

    predicted_price = predict_price(
        house_size,
        bedrooms,
        bathrooms,
        age,
        distance,
        parking
    )

    print("\nPredicted House Price: ₹", round(predicted_price, 2))
    import pandas as pd
import joblib
import os


# Load trained model
model_path = os.path.join(
    os.path.dirname(__file__),
    "house_price_model.pkl"
)

model = joblib.load(model_path)


def predict_price(
    house_size_sqft,
    bedrooms,
    bathrooms,
    age_years,
    distance_to_city_km,
    parking_spaces
):
    input_data = pd.DataFrame([{
        "house_size_sqft": house_size_sqft,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "age_years": age_years,
        "distance_to_city_km": distance_to_city_km,
        "parking_spaces": parking_spaces
    }])

    prediction = model.predict(input_data)

    return prediction[0]


if __name__ == "__main__":

    print("House Price Prediction")
    print("----------------------")

    house_size = float(input("Enter house size (sqft): "))
    bedrooms = int(input("Enter number of bedrooms: "))
    bathrooms = int(input("Enter number of bathrooms: "))
    age = int(input("Enter house age (years): "))
    distance = float(input("Enter distance to city (km): "))
    parking = int(input("Enter parking spaces: "))

    predicted_price = predict_price(
        house_size,
        bedrooms,
        bathrooms,
        age,
        distance,
        parking
    )

    print("\nPredicted House Price: ₹", round(predicted_price, 2))