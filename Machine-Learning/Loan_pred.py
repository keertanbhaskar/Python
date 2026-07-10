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


# ----------- Load Training Data -----------------
df = pd.read_csv("train_u6lujuX_CVtuZ9i.csv")

print(df.head())
print(df.info())
print(df.shape)

print("Missing Values Before Handling:")
print(df.isnull().sum())


# Handle Missing Values
df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df["Education"] = df["Education"].fillna(df["Education"].mode()[0])
df["Loan_Status"] = df["Loan_Status"].fillna(df["Loan_Status"].mode()[0])

df["ApplicantIncome"] = df["ApplicantIncome"].fillna(df["ApplicantIncome"].mean())
df["LoanAmount"] = df["LoanAmount"].fillna(df["LoanAmount"].mean())

print("Missing Values After Handling:")
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
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

# Accuracy
print("\nDecision Tree Accuracy :", accuracy_score(y_test, dt_pred))
print("Random Forest Accuracy :", accuracy_score(y_test, rf_pred))

# Load Test Dataset
new_data = pd.read_csv("test_Y3wMUE5_7gLdaTN.csv")

print("\nMissing Values in Test Data:")
print(new_data.isnull().sum())

# Handle Missing Values
new_data["Gender"] = new_data["Gender"].fillna(new_data["Gender"].mode()[0])
new_data["Education"] = new_data["Education"].fillna(new_data["Education"].mode()[0])

new_data["ApplicantIncome"] = new_data["ApplicantIncome"].fillna(new_data["ApplicantIncome"].mean())
new_data["LoanAmount"] = new_data["LoanAmount"].fillna(new_data["LoanAmount"].mean())

# Encode Test Data
new_data["Gender"] = le_gn.transform(new_data["Gender"])
new_data["Education"] = le_ed.transform(new_data["Education"])


# Prediction
X_new = new_data[["Gender", "Education", "ApplicantIncome", "LoanAmount"]]
prediction = dt.predict(X_new)
result = le_ls.inverse_transform(prediction)

print("Decision tree accuracy",accuracy_score(y_test,dt_pred))
print("Random forest accuracy:",accuracy_score(y_test,rf_pred))
print("\nPrediction for First Applicant :", result[0])


# Decision Tree graph
plt.figure(figsize=(15, 8))

plot_tree(
    dt,
    feature_names=X.columns,
    class_names=["N", "Y"],
    filled=True,
    rounded=True
)

plt.title("Decision Tree")
plt.show()