from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

# Dataset
data = {
    'Python': [9,8,2,3,8,7,4,3,5,9,2,8],
    'Java': [3,2,9,10,2,3,3,2,4,1,8,2],
    'WebDev': [2,3,3,2,9,10,2,1,3,4,4,8],
    'ML': [10,9,1,1,2,2,1,2,2,8,1,3],
    'DevOps': [1,2,2,1,3,2,10,9,8,2,1,2],
    'DSA': [7,8,8,9,7,8,7,8,9,6,7,7],
    'JobRole': [
        'ML Engineer',
        'ML Engineer',
        'Java Developer',
        'Java Developer',
        'Full Stack Developer',
        'Full Stack Developer',
        'DevOps Engineer',
        'DevOps Engineer',
        'DevOps Engineer',
        'ML Engineer',
        'Java Developer',
        'Full Stack Developer'
    ]
}

