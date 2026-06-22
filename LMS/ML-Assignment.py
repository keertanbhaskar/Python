import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "marks":       [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90],
    "result":      [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[['study_hours']]
y = df[['result']]

X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.2,random_state=42)

model = LogisticRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
print("Accuracy:",accuracy_score(y_test,y_pred))
print("Confusion Matrix:\n",confusion_matrix(y_test,y_pred))


test_study_hour = [[2]]
print('will pass?',model.predict(test_study_hour))


plt.scatter(X, y,color='green')
plt.plot(X,model.predict(X),color='red')
plt.xlabel('Marks')
plt.ylabel("Result (0=Fail, 1=pass)")
plt.title("Pass/Fail prediction")
plt.show()
