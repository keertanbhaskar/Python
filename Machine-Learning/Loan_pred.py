# Dataset: “Loan Prediction Problem Dataset”
# Features: Gender, Education, Income, LoanAmount
# Label: Loan_Status (Y/N)

from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv('train_u6lujuX_CVtuZ9i.csv')
print(df.head(5))
print(df.info())

le = LabelEncoder()

df['Gender'] = le.fit_transform(df['Gender'])
df['Education'] = le.fit_transform(df['Education'])
df['Loan_Status'] = le.fit_transform(df['Loan_Status'])


X = df[['Gender', 'Education', 'ApplicantIncome', 'LoanAmount']]
y = df['Loan_Status']

# split data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)


# Decision tree
dt = DecisionTreeClassifier()
dt.fit(X_train,y_train)
dt_pred = dt.predict(X_test)

# Random forest
rf = RandomForestClassifier()
rf.fit(X_train,y_train)
rf_pred = rf.predict(X_test)

# accuracy
print("Decision Tree Acc:",accuracy_score(y_test,dt_pred))
print("Random Forest Acc:",accuracy_score(y_test,rf_pred))

# Decision tree
plt.figure(figsize=(15,8))
plot_tree(
  dt,feature_names=X.columns,
  class_names=['N',"Y"],
  filled=True
)

plt.show()

