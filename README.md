# House-Price-Prediction
# 🏠 House Price Prediction using Linear Regression

## 📌 Project Overview

This project is a simple Machine Learning model that predicts **house prices based on the area of the house in square feet**.

The project uses **Linear Regression** to learn the relationship between house area and price.

## 🎯 Objective

The main objective of this project is to build a Machine Learning model that can predict house prices using the **Area** of the house as the input feature.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib

## 📊 Dataset

The dataset is stored in:

`house_price.csv`

The project uses:

* **Feature (X):** Area
* **Target (y):** Price

Example:

| Area |   Price |
| ---: | ------: |
| 1000 |  500000 |
| 1500 |  750000 |
| 2000 | 1000000 |

## 🔄 Project Workflow

1. Load the dataset using Pandas
2. Select `Area` as the input feature
3. Select `Price` as the target variable
4. Split the dataset into training and testing data
5. Train a Linear Regression model
6. Make predictions on the test data
7. Evaluate the model using MAE, MSE and RMSE
8. Display the regression equation parameters
9. Save the trained model using Joblib

## 🤖 Machine Learning Model

The project uses **Linear Regression**.

The basic relationship is:

**Price = Intercept + (Coefficient × Area)**

The model learns the intercept and coefficient from the training data.

## 📈 Model Evaluation

The following metrics are used to evaluate the model:

* **MAE (Mean Absolute Error)**
* **MSE (Mean Squared Error)**
* **RMSE (Root Mean Squared Error)**

Run the Python program to see the actual values for these metrics.

## 💾 Saved Model

After training, the model is saved as:

`house_price_model.pkl`

This saved model can later be loaded and used to make predictions without training the model again.

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Install the required libraries

```bash
pip install pandas numpy scikit-learn joblib
```

### 3. Make sure these files are in the project folder

```text
House-Price-Prediction/
│
├── house_price.csv
├── house_price_model.pkl
├── main.py
└── README.md
```

### 4. Run the Python file

```bash
python main.py
```

## 📌 Example Output

```text
MAE: 38341.204476421066
MSE: 3418946311.180807
RMSE: 58471.75652552955
Intercept: 24899.74815733818
Coefficient: 102.48895891672333
```

The exact values depend on the dataset used for training and testing.

## 🚀 Future Improvements

Some possible improvements for this project are:

* Add more features such as number of bedrooms, bathrooms and location
* Perform more detailed Exploratory Data Analysis
* Compare Linear Regression with other Machine Learning algorithms
* Build a simple web interface for house price prediction
* Deploy the model as a web application

## 👨‍💻 Author

**Anjana Devi**

Machine Learning | Python | Data Science

