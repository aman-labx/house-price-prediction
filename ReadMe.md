# 🏠 House Price Prediction

A beginner Machine Learning project that predicts house prices using
property-related features and Linear Regression.

The project also includes a Flask web application that allows users
to enter property details and receive a predicted house price.

---

## 📌 Project Objective

The goal of this project is to understand the complete basic Machine
Learning workflow:

- Data generation
- Data exploration
- Data visualization
- Feature selection
- Train/test split
- Linear Regression
- Model evaluation
- Model saving
- Prediction
- Flask web integration

---

## 🧠 Machine Learning Model

The project uses:

**Linear Regression**

The trained model predicts house prices using six features:

1. House size
2. Number of bedrooms
3. Number of bathrooms
4. House age
5. Distance to city
6. Parking spaces

### Target

```text
price
📊 Dataset

The dataset contains 300 synthetic records.

The data was generated for learning purposes and does not represent
real-world housing market data.

Because the target price was generated using a formula based on the
same input features, the model achieves a very high R² score on this
synthetic dataset.

This should not be interpreted as real-world prediction accuracy.

📈 Model Evaluation

The Linear Regression model was evaluated using:

MAE: 125058.79
MSE: 23867750545.69
R² Score: 1.0

These results are specific to the synthetic dataset used in this
learning project.

🌐 Web Application

A Flask-based web interface is included in the project.

Users can enter:

House size
Bedrooms
Bathrooms
House age
Distance to city
Parking spaces

The web application sends the data to the Flask backend, which loads
the trained Machine Learning model and returns the predicted price.

Web Application Flow

User Input
    ↓
HTML Form
    ↓
JavaScript
    ↓
Flask API
    ↓
Trained ML Model
    ↓
Prediction
    ↓
Web Interface
🛠️ Technologies
Machine Learning
Python
Pandas
NumPy
Scikit-learn
Joblib
Data Visualization
Matplotlib
Seaborn
Web Development
Flask
HTML
CSS
JavaScript
Tools
VS Code
Jupyter Notebook
Git
GitHub

📁 Project Structure

house-price-prediction/
│
├── data/
│   └── house_data.csv
│
├── notebooks/
│   └── house_price_prediction.ipynb
│
├── src/
│   ├── model.py
│   └── house_price_model.pkl
│
├── web/
│   ├── app.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       ├── style.css
│       └── script.js
│
├── .gitignore
├── README.md
└── requirements.txt

⚙️ Installation

Clone the repository:

git clone https://github.com/aman-labx/house-price-prediction.git

Move into the project directory:

cd house-price-prediction

Install dependencies:

python -m pip install -r requirements.txt
▶️ Run the Machine Learning Prediction Script

Run:

python src\model.py

The program will ask for property information and return a predicted
house price.

🌐 Run the Web Application

Start the Flask server:

python web\app.py

Then open:

http://127.0.0.1:5000

🔮 Future Improvements

Possible improvements include:

Use a real-world housing dataset
Compare multiple regression models
Improve feature engineering
Add more evaluation metrics
Add data validation
Deploy the Flask application
Add interactive visualizations
Experiment with Random Forest and other models
📚 Learning Outcome

This project helped me understand how a Machine Learning model can
move from a dataset and notebook into a simple working application.

The project is part of my ongoing Machine Learning learning journey.

👨‍💻 Author

Aman Machhirke

1st Year Computer Engineering (AI & ML) Student

GitHub:

https://github.com/aman-labx

⚠️ Disclaimer

This is a beginner educational project.

The dataset is synthetic and the model is not intended for real-world
property valuation or financial decision-making.