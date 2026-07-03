from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,precision_score, recall_score, f1_score


# Sample data
messages = ["Win cash now", "Your OTP is 4567", "Free vacation offer", "Let's meet tomorrow"]
labels = [1, 0, 1, 0]  # 1 = Spam, 0 = Not spam

# Convert text to numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# train-test split
X_train, X_test, y_train, y_test = train_test_split(X,labels,test_size=0.25)

# train Model
model = LogisticRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

# predict
prediction = model.predict(vectorizer.transform(['Congrats, you won!']))
print('is spam:',bool(prediction[0]))


print(classification_report(y_test,y_pred))


print('Precision score:',precision_score(y_test,y_pred))
print(recall_score(y_test, y_pred))
f1 = f1_score(y_test, y_pred)
print(f"f1 score:{f1}")
