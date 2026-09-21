# 🏠 House Price Prediction

A beginner machine learning project that predicts house prices based on property features such as size, bedrooms, bathrooms, age, distance from the city, and parking spaces.

This project was built as part of my machine learning learning journey.

---

## 📌 Project Objective

The goal of this project is to understand the basic machine learning workflow for a regression problem:

- Creating a dataset
- Exploring and understanding data
- Visualizing relationships between features
- Splitting data into training and testing sets
- Training a Linear Regression model
- Making predictions
- Evaluating model performance
- Saving and using a trained machine learning model

---

## 🧠 Machine Learning Approach

This project uses **Linear Regression** to predict house prices.

### Input Features

| Feature | Description |
|---|---|
| `house_size_sqft` | House size in square feet |
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms |
| `age_years` | Age of the house |
| `distance_to_city_km` | Distance from the city in kilometers |
| `parking_spaces` | Number of parking spaces |

### Target

`price`

The target represents the generated house price.

---

## 📊 Dataset

The dataset contains **300 synthetic house records**.

The data was generated using Python and NumPy for learning purposes.

The house price was generated using a formula based on the input features with added random noise.

Therefore, this dataset should **not** be considered real-world housing market data.

---

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

---

## 📂 Project Structure

```text
house-price-prediction/
│
├── data/
│   └── house_data.csv
│
├── notebooks/
│   └── house_price_prediction.ipynb
│
├── src/
│   ├── house_price_model.pkl
│   └── model.py
│
├── .gitignore
├── README.md
└── requirements.txt
🔬 Project Workflow
Dataset Creation
       ↓
Data Exploration
       ↓
Data Visualization
       ↓
Correlation Analysis
       ↓
Train/Test Split
       ↓
Linear Regression
       ↓
Prediction
       ↓
Model Evaluation
       ↓
Save Trained Model
       ↓
Terminal Prediction
📈 Model Evaluation

The Linear Regression model produced the following results on the test dataset:

Metric	Result
MAE	125,058.79
MSE	23,867,750,545.69
R² Score	1.00
Metric Explanation

MAE — Mean Absolute Error

The average absolute difference between the actual and predicted prices.

MSE — Mean Squared Error

Measures the squared prediction error and gives greater weight to larger errors.

R² Score

Measures how much of the variation in the target is explained by the model.

⚠️ Important Limitation

The dataset used in this project is synthetic.

The target price was generated using a mathematical formula based on the same features used by the model. Because of this, the model can achieve a very high R² score.

Therefore, the R² = 1.00 result should not be interpreted as evidence that the model would achieve perfect performance on real-world housing data.

A real-world project would require a larger and representative housing dataset, additional relevant features, and more rigorous validation.

▶️ How to Run
1. Clone the repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
2. Open the project
cd house-price-prediction
3. Install dependencies
pip install -r requirements.txt
4. Run the prediction program
python src/model.py

The program will ask for:

House size
Number of bedrooms
Number of bathrooms
House age
Distance to city
Parking spaces

It will then display the predicted house price.

💻 Example
House Price Prediction
----------------------
Enter house size (sqft): 2000
Enter number of bedrooms: 3
Enter number of bathrooms: 2
Enter house age (years): 10
Enter distance to city (km): 5
Enter parking spaces: 1

Predicted House Price: ₹XXXXXXXX

The exact prediction depends on the trained model.

📚 What I Learned

Through this project, I practiced:

Working with Pandas DataFrames
Creating synthetic datasets
Data exploration
Data visualization
Correlation analysis
Feature/target separation
Train/test splitting
Linear Regression
Model prediction
MAE, MSE and R²
Saving trained models with Joblib
Loading a trained model in another Python script
Making predictions through the terminal
🚀 Future Improvements

Possible improvements for a future version:

Use a real-world housing dataset
Perform more extensive data preprocessing
Compare multiple regression algorithms
Perform cross-validation
Tune model parameters
Add more relevant housing features
Build a web interface for predictions
Deploy the model as a small ML application
👨‍💻 Author

Aman Machhirke

1st Year College Student
Aspiring Machine Learning Engineer

This project is part of my journey of learning Python, data science and machine learning.

⚠️ Disclaimer

This project is created for educational and learning purposes.

The dataset is synthetic and the predicted prices should not be used for real-world property valuation or financial decisions.