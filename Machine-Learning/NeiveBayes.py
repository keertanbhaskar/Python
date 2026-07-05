from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# sample msg
texts = [
    "Win cash now",
    "Free vacation offer",
    "Claim your reward",
    "Exclusive discount",
    "You won lottery",
    "Get free money",
    "Let's meet tomorrow",
    "Project discussion",
    "Your OTP is 123456",
    "Call me tonight",
    "Submit assignment",
    "See you in class",
    "Meeting at 5 PM",
    "Dinner tonight",
    "Happy birthday"
]

labels = [
    1,1,1,1,1,1,
    0,0,0,0,0,0,0,0,0
]


# convert text to feature vectors
vectorize = CountVectorizer()
X = vectorize.fit_transform(texts)


# train-test split
X_train, X_test, y_train, y_test = train_test_split(X,labels,test_size=0.25)


# train Naive Bayes model
model = MultinomialNB()
model.fit(X_train,y_train)

# predict
y_pred = model.predict(X_test)
msg = ["Exclusive offer just for you"]
X_msg = vectorize.transform(msg)
print(classification_report(y_test,y_pred))
print('spam?' if model.predict(X_msg)[0] else 'Not Spam')
