import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Mall_Customers.csv')

df.groupby('Gender')['Spending Score (1-100)'].count().plot(kind='bar')
plt.xlabel('Gender')
plt.ylabel('Count of Customers')
plt.title('Number of Customers by Gender')
plt.show()

df.groupby('Annual Income (k$)')['Spending Score (1-100)'].mean().plot(kind='line')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Average Spending Score')
plt.title('Average Spending Score by Annual Income')
plt.show()