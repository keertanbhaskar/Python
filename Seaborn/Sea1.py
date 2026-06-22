import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.scatterplot(
    x="total_bill",
    y="tip",
    data=tips
)

# plt.xlabel("Total Bill")
# plt.ylabel("Tip Amount")
plt.title("Bill vs Tip")
plt.legend(["Customers"])

plt.show()