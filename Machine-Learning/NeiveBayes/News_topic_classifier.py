import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report,accuracy_score

df = pd.read_csv('NeiveBayes/train.csv')
print(df.head())
print(df.info())
print(df.shape)
print(df.isnull().sum())

print(df.columns)


features = df['Description']
y = df['Class Index']

tfi = TfidfVectorizer()
X = tfi.fit_transform(features)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)


model = MultinomialNB()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)


print(classification_report(y_test,y_pred))


test_data = pd.read_csv('NeiveBayes/test.csv')
print(test_data.isnull().sum())

test_des = tfi.transform(test_data['Description'])
test_pred = model.predict(test_des)

print('the prediction:',test_pred[0])

print("Acuuracy:",accuracy_score(y_test,y_pred))






