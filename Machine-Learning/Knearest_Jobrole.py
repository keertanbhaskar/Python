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


skills = ["HTML_CSS", "JavaScript", "Python", "ML", "Linux", "Docker", "Creativity"]

ratings = []

for skill in skills:
    while True:
        rating = int(input(f"Rate {skill} (1-5): "))
        if 1 <= rating <= 5:
            ratings.append(rating)
            break
        else:
            print("Invalid rating! Please enter a value between 1 and 5.")

new_candidate = pd.DataFrame([ratings], columns=skills)


prediction = model.predict(new_candidate)
print(le.inverse_transform(prediction))



