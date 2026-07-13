# Dataset: Loan Prediction Problem Dataset
# Features: Gender, Education, ApplicantIncome, LoanAmount
# Label: Loan_Status (Y/N)

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("train_u6lujuX_CVtuZ9i.csv")

print(df.head())
print(df.info())
print(df.shape)


print(df.isnull().sum())



df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df["Education"] = df["Education"].fillna(df["Education"].mode()[0])
df["Loan_Status"] = df["Loan_Status"].fillna(df["Loan_Status"].mode()[0])

df["ApplicantIncome"] = df["ApplicantIncome"].fillna(df["ApplicantIncome"].mean())
df["LoanAmount"] = df["LoanAmount"].fillna(df["LoanAmount"].mean())

# check the missing value after the data handling
print(df.isnull().sum())


# Label Encoding
le_gn = LabelEncoder()
le_ed = LabelEncoder()
le_ls = LabelEncoder()

df["Gender"] = le_gn.fit_transform(df["Gender"])
df["Education"] = le_ed.fit_transform(df["Education"])
df["Loan_Status"] = le_ls.fit_transform(df["Loan_Status"])

# Features & Target
X = df[["Gender", "Education", "ApplicantIncome", "LoanAmount"]]
y = df["Loan_Status"]


# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Decision Tree 

dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

dt_pred = dt.predict(X_test)






# Random Forest Model
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)



# Accuracy
print("Decision Tree Acc:", accuracy_score(y_test, dt_pred))
print("Random Forest Acc:", accuracy_score(y_test, rf_pred))

#  Test Dataset
test_data = pd.read_csv("test_Y3wMUE5_7gLdaTN.csv")

print("Missing Values in  Data:")
print(test_data.isnull().sum())


test_data["Gender"] = test_data["Gender"].fillna(test_data["Gender"].mode()[0])
test_data["Education"] = test_data["Education"].fillna(test_data["Education"].mode()[0])
test_data["ApplicantIncome"] = test_data["ApplicantIncome"].fillna(test_data["ApplicantIncome"].mean())
test_data["LoanAmount"] = test_data["LoanAmount"].fillna(test_data["LoanAmount"].mean())


test_data["Gender"] = le_gn.transform(test_data["Gender"])
test_data["Education"] = le_ed.transform(test_data["Education"])


# Prediction
X_new = test_data[["Gender", "Education", "ApplicantIncome", "LoanAmount"]]
prediction = dt.predict(X_new)
# result = le_ls.inverse_transform(prediction)

print("Decision tree accuracy",accuracy_score(y_test,dt_pred))
print("Random forest accuracy:",accuracy_score(y_test,rf_pred))
print("Prediction for First Applicant :", prediction[0])


# Decision Tree graph
plt.figure(figsize=(15, 8))

plot_tree(
    dt,
    feature_names=["Gender", "Education", "ApplicantIncome", "LoanAmount"],
    filled=True
)

plt.title("Decision Tree")
plt.show()