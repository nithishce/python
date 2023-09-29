import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('cars.csv')

print(df)

print(df.head())

print(df.info())

print(df.describe())

print(df.shape)

print(df.columns)

print(df[df.isnull()].count())

print(df[df.duplicated()].count())


print(df[df.Make =='Tata'].tail())


#pie
fig = plt.figure(figsize = (10,10))
ax = fig.subplots()
df.Make.value_counts().plot(ax=ax, kind='pie')
ax.set_ylabel("")
ax.set_title("Top Car Making Companies in India")
plt.show()

#pie
fig = plt.figure(figsize = (10,10))
ax = fig.subplots()
df.Fuel_Type.value_counts().plot(ax=ax, kind='pie')
ax.set_ylabel("")
ax.set_title("Cars Count by Engine Fuel Type")
plt.show()

# Bar plot
plt.figure(figsize=(10, 6))
sns.countplot(x='Body_Type', data=df)
plt.xlabel('Body Type')
plt.ylabel('Count')
plt.title('Bar Plot of Cars by car body type')
plt.xticks(rotation=45)  
plt.show()


