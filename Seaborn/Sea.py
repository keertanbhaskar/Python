import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# loading dataset
df = sns.load_dataset('tips')
# print(df.head())

# distribution plots
sns.histplot(df['total_bill'],kde=True)
plt.show()

# KDE plot
sns.kdeplot(df['total_bill'])
plt.show()


# ==========Categorical Plots==========


# 1.count plot
sns.countplot(x='sex',data=df,hue='smoker',edgecolor='black',palette='Set2')
plt.title("countplot")
plt.show()


# 2.Bar plot 
sns.barplot(x='day',y='total_bill',data=df)
plt.show()

# 3.Violin plot
sns.violinplot(x='day',y='total_bill',data=df)
plt.show()



# =============Relationship plots==========

# scatter plot
sns.scatterplot(x='total_bill',y='tip',data=df)
plt.show()

# 2.Regression plot => adds trend line
sns.regplot(x='total_bill',y='tip',data=df)
plt.show()


# ======= multivariable Analysis =======

# 1.Hue parameter
sns.scatterplot(x='total_bill',y='tip',hue='sex',data=df)
plt.title('Hue')
plt.show()


# ============ correlation analysis ===========

# 1.Correlation matrix
corr = df.corr(numeric_only=True)
plt.title('correlation')
print(corr)



# 2.HeatMap
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.title('heatmap')
plt.show()






# =============== FaceGrid ==========
g = sns.FacetGrid(
  df,
  col='sex'
)

g.map(
  plt.hist,'total_bill'
)
plt.title('facegrid')
plt.show()



# ======= box plot ==============
sns.boxplot(x='day',y='total_bill',data=df)
plt.title("total distribution by day")
plt.show()





# ----------- line plot ------------
sns.lineplot(
    x="day",
    y="total_bill",
    data=df,
    marker="o"
)

plt.title("Average Total Bill by Day")
plt.show()

# ========= pair plot ========
sns.pairplot(df)
plt.title('Pair plot')
plt.show()
