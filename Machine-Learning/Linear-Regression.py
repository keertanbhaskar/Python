from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# example data
X = [[1000],[1500],[2000],[2500]] #Area
y = [4000000,5500000,7000000,8500000] #Price

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train,y_train)

# predict
predicted_price = model.predict([[1200]])
print(f"Predicted Price for 1200 sqft:₹{predicted_price[0]:,.0f}")


# Evaluation Metrics
y_pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))