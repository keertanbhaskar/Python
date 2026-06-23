# predict marks based on hours studied

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

data = {

    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    "marks": [35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

}

df = pd.DataFrame(data)

X = df[['study_hours']]
y = df['marks']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
print("Predictions:",y_pred)
print("MSE:",mean_squared_error(y_test,y_pred))
print("R² Score:",r2_score(y_test,y_pred)) 


hours = [[6.5]]
pred_marks = model.predict(hours)
print("Predicted marks for 6.5 hours:",pred_marks)


# visualizing the result
plt.scatter(X,y,color='blue',label='actual')
plt.plot(X,model.predict(X),color='red',label='prediction line')
plt.xlabel('Study hours')
plt.ylabel('marks')
plt.title('Study Time vs Marks Prediction') 
plt.legend()
plt.grid()
plt.show()

