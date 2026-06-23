import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\basav\\OneDrive\\Documents\\OneDrive\\Desktop\\Python\\LMS\\Students1.csv")

# data cleaning
print(df.info())
print(df.isnull().sum())

X = df[['study_hours','attendance','previous_marks']]
y = df['result']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=1)

model = LogisticRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
print("Accuracy:",accuracy_score(y_test,y_pred))
print("Confusion Matrix:\n",confusion_matrix(y_test,y_pred))


new_data = [[6,70,60]]
print("Will pass?",model.predict(new_data)[0])


sns.heatmap(confusion_matrix(y_test,y_pred),annot=True,fmt='d',cmap='Blues')
plt.title('confusion matrix')
plt.xlabel('predicted')
plt.ylabel("Actual")
plt.show()