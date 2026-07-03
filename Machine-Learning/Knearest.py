# Movie Recommender

from sklearn.neighbors import KNeighborsClassifier
# Feature = [action_rating, romance_rating]
X  = [[5,1],[1,5],[4,2],[2,4],[3,5]]
y = ["Action", "Romance", "Action", "Romance", "Romance"]

# new user's preference
new_user = [[4,1]]
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X,y)
prediction = model.predict(new_user)
print('Recommender Genre:',prediction[0])