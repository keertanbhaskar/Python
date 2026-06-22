import numpy as np
import pandas as pd
from scipy import stats


scores = np.array([85,90,75,80,85,92,88])


# mean
print("Mean:", np.mean(scores))


# median
print("Median:", np.median(scores))


# mode
print("Mode:",stats.mode(scores,keepdims=True).mode[0])



# variance
print("Variance:",np.var(scores))

# standard deviation
print("Standard Deviation:", np.std(scores))


# ========== Probability ==========

grades = pd.Series(['A', 'B', 'A', 'C', 'B', 'B'])
probs = grades.value_counts(normalize=True)



# ============ Normal Distribution ===========
import matplotlib.pyplot as plt
import seaborn as sns


data = np.random.normal(loc=70,scale=10,size=1000)
sns.histplot(data,kde=True)
plt.title("Noraml Distribution of scores")
plt.show()






print("============= Assignment: Student Score Statistics ============ ")
arr = np.array([85, 78, 92, 75, 85, 90, 68, 70, 88, 95])

print("Mean:",np.mean(arr))
print("Median:",np.median(arr))
print("Mode:",stats.mode(scores,keepdims=True).mode[0])
print("Variance:",np.var(arr))
print("Std:",np.std(arr))

mean_val = np.mean(arr)
std_val = np.std(arr)

students = np.random.normal(mean_val, std_val, 1000)
sns.histplot(students,kde=True,bins=30)
plt.title("Student score distribution")
plt.show()



