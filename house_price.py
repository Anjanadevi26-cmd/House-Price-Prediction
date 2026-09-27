import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import joblib
# Load dataset
df = pd.read_csv("house_price.csv")

# Features and target
X = df[["Area"]]   # Feature (square feet)
y = df["Price"]    # Target (house price)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

#save model
joblib.dump(model, 'house_price_model.pkl')
# Predictions
y_pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)

# Show regression equation
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_[0])

