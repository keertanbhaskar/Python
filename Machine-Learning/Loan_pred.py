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

le_gn = LabelEncoder()
le_ed = LabelEncoder()
le_lnSt = LabelEncoder()

df['Gender'] = le_gn.fit_transform(df['Gender'])
df['Education'] = le_ed.fit_transform(df['Education'])
df['Loan_Status'] = le_lnSt.fit_transform(df['Loan_Status'])


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


# testing
new_data = pd.read_csv('test_Y3wMUE5_7gLdaTN.csv')
new_data['Gender'] = le_gn.fit_transform(new_data['Gender'])
new_data['Education'] = le_gn.fit_transform(new_data['Education'])

X_new = new_data[['Gender','Education','ApplicantIncome', 'LoanAmount']]
prediction = dt.predict(X_new)
result = le_lnSt.inverse_transform(prediction)
print("New Prediction of decision tree:",result[0])


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

