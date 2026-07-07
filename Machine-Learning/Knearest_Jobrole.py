from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv('job_roles.csv')
print(df.head())
print(df.shape)


X = df.drop('JobRole',axis=1)
y = df['JobRole']

le = LabelEncoder()
y = le.fit_transform(y)

model = KNeighborsClassifier()
model.fit(X,y)

new_candidate = pd.DataFrame([[5,5,2,1,2,1,3]],columns=X.columns)
prediction = model.predict(new_candidate)
print(le.inverse_transform(prediction))



