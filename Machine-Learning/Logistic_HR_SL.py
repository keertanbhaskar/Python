import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,f1_score,precision_score,recall_score
from sklearn.preprocessing import LabelEncoder

# data
df = pd.read_csv("resume_dataset_200k_enhanced.csv")
print(df.head(5))
print(df.shape)

# features and labels
X = df[['education_level','cgpa','internships','projects','experience_years','skills_score','soft_skills_score']]
y = df['hired']


le = LabelEncoder()
X['education_level'] = le.fit_transform(X['education_level'])

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LogisticRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

print(classification_report(y_test,y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))

new_candidate = [[
    le.transform(['Bachelors'])[0],  # education_level
    8.5,    # cgpa
    3,      # internships
    5,      # projects
    1.5,    # experience_years
    18.0,   # skills_score
    8.0     # soft_skills_score
]]

prediction = model.predict(new_candidate)
if prediction[0] == 1:
  print('Hired')
else:
  print('Not hired')






