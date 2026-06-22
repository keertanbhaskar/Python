import matplotlib.pyplot as plt


# 1.Line plot
tests = [1,2,3,4]
scores = [70,75,80,85]
plt.plot(tests,scores)
plt.title('Test Progress')
plt.xlabel('Test Number')
plt.ylabel('Score')
plt.grid()
plt.show()






# 2.Bar Chart
names = ['Riya','Aman','Dev']
marks = [85,78,92]
plt.bar(names,marks,color='skyblue')
plt.title('Student Marks')
plt.xlabel('students')
plt.ylabel('marks')
plt.show()







# Histogram
scores = [65,70,75,80,85,90,95,100]
plt.hist(scores,bins=5,color='orange',edgecolor='black')
plt.title('Score Distribution')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()




# ====================== Seaborn ====================
import seaborn as sns
import pandas as pd

data = {

    "student": ["Riya", "Aman", "Dev", "Sara"],
    "marks": [85, 78, 92, 88],
    "subject": ["Math", "Science", "Math", "Science"]

}


df = pd.DataFrame(data)
sns.barplot(x='student', y='marks', data=df)
plt.title('Marks by Student')
plt.show()





# Heatmaps
matrix = [[70,80],[85,90]]
sns.heatmap(matrix, annot=True, cmap='YlGnBu')
plt.title('Heatmap of Marks')
plt.show()





# ============ Assignment ==============

# load data
df1 = pd.read_csv('students.csv')


# add grade column
def grade(marks):
  if marks >= 90:
    return 'A'
  elif marks >= 75:
    return 'B'
  elif marks >= 60:
    return 'C'
  else:
    return 'F'
  
df1['Grade'] = df1['marks'].apply(grade)


# create bar chart
sns.barplot(x='name', y='marks', data=df1)
plt.title('names vs marks')



# line chart
sub_avg = df1.groupby('subject')['marks'].mean()
plt.plot(sub_avg.index,sub_avg.values, marker='o')
plt.xlabel('Subjects')
plt.ylabel('Average Marks')
plt.grid(True)
plt.show()


# HeatMap
heatmap_data = pd.DataFrame(df.groupby('subject')['marks'].mean())
sns.heatmap(
    heatmap_data,
    annot=True,
    cmap='YlGnBu'
)

plt.title("Subject-wise Average Marks")
plt.show()


