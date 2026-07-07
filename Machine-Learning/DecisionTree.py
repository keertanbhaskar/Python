from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt

# ex: [age,income in ₹1k]
X = [[25,30],[45,80],[35,40],[50,90],[28,25]]
y = ['No','Yes','Yes','Yes','No'] #loan approved

# Train/test 
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
model = DecisionTreeClassifier()
model.fit(X_train,y_train)

# Predict
print(model.predict([[40,60]]))


# visualizing the tree
plt.figure(figsize=(10,6))
tree.plot_tree(model,filled=True)
plt.show()

rd = RandomForestClassifier()
rd.fit(X_train,y_train)
print(model.predict([[40,60]]))