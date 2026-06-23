import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("house_price.csv")

# Features and Target
X = df[['size']]
y = df['price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Evaluation
print("Predictions:", y_pred)
print("Actual:", list(y_test))

print("MSE:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Predict new house size
new_size = [[750]]

predicted_price = model.predict(new_size)

print(f"Predicted price for {new_size[0][0]} sq ft:",
      predicted_price[0])

# Visualization
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X), color="red", label="Regression Line")

plt.xlabel("Size (sq ft)")
plt.ylabel("Price")
plt.title("House Price Prediction")
plt.legend()
plt.grid()

plt.show()