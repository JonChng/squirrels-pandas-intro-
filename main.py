import pandas as pd



data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

count = data["Primary Fur Color"].value_counts()
print(count)
headings = ["Fur Color", "Count"]

df = pd.DataFrame(count).reset_index()
df.columns = headings
df.to_csv("squirrel_count.csv")




