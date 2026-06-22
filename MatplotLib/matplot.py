import matplotlib.pyplot as plt

# Line Plot => Trends, Growth
month = ['jan','feb','march',"apr"]
sales = [10000,12000,18000,25000]

plt.plot(month,sales,color='red',linestyle="--",linewidth=4,marker='o',label="Sales")
plt.legend()
plt.title("Monthly Sales")
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid(True)
plt.show()





# Bar Chart => used for comparison
courses = ['py','java','sql','Devops']
students = [120,90,60,80]

plt.bar(courses,students,color='green',edgecolor='black')
plt.title("Students Enrolled in Courses")
plt.xlabel("Courses")
plt.ylabel("Number of Students")
plt.show()



# horizontal bargraph
plt.barh(courses,students,color=['green','red','skyblue','purple'],edgecolor='black')
plt.title("Students Enrolled in Courses")
plt.xlabel("Courses")
plt.ylabel("Number of Students")
plt.show()




# histogram => Shows distribution.
salaries = [
    25000, 27000, 28000, 30000,
    32000, 35000, 36000, 40000,
    42000, 48000, 50000
]
plt.hist(salaries, bins=5,edgecolor='red')
plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.show()




# pie chart
languages = ["Python","Java","C++"]
students = [50,30,20]
plt.pie(students,labels=languages,autopct="%1.1f%%")
plt.title('Programming language distribution')
plt.show()



# Scatter plot => shows relationship
hours = [1,2,3,4,5]
marks = [40,50,65,75,90]
plt.figure(figsize=(10,5))
plt.scatter(hours,marks,marker='+',label="Student Data")
plt.legend()
plt.show()




# subplots => display multiple charts together
plt.subplot(1,2,1)
plt.plot([1,2,3],[4,5,6])
plt.subplot(1,2,2)
plt.bar([1,2,3],[4,5,6])
plt.tight_layout()
plt.show()







months = ["January", "February", "March", "April"]
sales = [10, 20, 15, 25]
plt.plot(months, sales)
plt.xticks(rotation=45)
plt.show()




# Assignment
import pandas as pd
df = pd.read_csv('students.csv')


# -------- bar chart --------------
plt.bar(df['name'],df['marks'])
plt.title('names vs marks')
plt.show()

# ========= histogram =========
plt.hist(df['marks'])
plt.title("distribution of marks")
plt.show()


# ======== line chart ==========
sub_avg = df.groupby('subject')['marks'].mean()
plt.plot(sub_avg.index,sub_avg.values)
plt.show()