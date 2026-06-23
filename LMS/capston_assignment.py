# =========== health risk ================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("cap_healthRisk.csv")

X = df[['age','bmi','smoking','activity']]
y = df['risk_level']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
print("accuracy score",accuracy_score(y_test,y_pred))
print("\nConfusion Matrix:",confusion_matrix(y_test, y_pred))
test_data = pd.DataFrame({
    'age':[23],
    'bmi':[20.1],
    'smoking':[0],
    'activity':[4]
})

print("resk_level:",model.predict(test_data)[0])


