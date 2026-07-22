
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = load_iris(as_frame=True)
X = data.data
y = data.target

# train and save the model
model = RandomForestClassifier()
model.fit(X,y)

joblib.dump(model,'iris_model.pkl')