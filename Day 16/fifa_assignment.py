""" Aaryan Pal """
import pandas as pd
from plotnine import ggplot, aes, geom_point, labs, geom_line, geom_bar


""" Read CSV File """
df1 = pd.read_csv("FIFA17_official_data.csv")
print("First 5 records")
print(df1.head())


""" Data Preparation """
# Create dataframe with columns: "Name" and "Best Overall Rating"
df = df1[['Name', 'Best Overall Rating']]
# Drop Records with NaN values
df = df.dropna()
# Drop duplicate values in column: "Name" but keep first entry
df.drop_duplicates('Name', inplace=True, keep='first')
# Sort the data in descending order by "Best Overall Rating"
df.sort_values(by='Best Overall Rating', ascending=False, inplace=True)


""" Plot the Best 5 Players on a bar plot """
best_5 = df.head()
print("Top 5 Players:")
print(best_5)

# Bar Plot of top 5 Players
match = ["red", "green", "yellow", "blue", "violet"]
# Add annotations for clarity
# for i in range(2):
#     count = df["survived"].value_counts()[i]
#     plt.annotate(f"{count}", xy = (i, count), ha = "center", va = "bottom")
bar_5 = (ggplot(best_5, aes(x=best_5['Name'], y=best_5['Best Overall Rating'])) + geom_bar(stat="identity", fill=match, alpha=0.7) + labs(x="Player", y="Rating", title="Top 5 Players & Ratings"))
print(bar_5)


""" Ashutosh Awasthi """
# import pandas as pd
# from plotnine import ggplot,aes,geom_point,labs,geom_line,geom_bar
# df=pd.read_csv("FIFA17_official_data.csv")
# print("All")
# print(df.head())
#
# print("Two columns")
# #data_preparation
# df2=df[["Name","Best Overall Rating"]]
# print(df2)
#
# print("na dropped")
# #dropping_na_values
# df2=df2.dropna()
# print(df2)
#
#
#
#
# #dropping_duplicates
# df2=df2.drop_duplicates(subset=["Name"],keep='first')
# print(df2)
#
#
# #sort_values
# df2.sort_values(by="Best Overall Rating",ascending=[False],inplace =True)
# print(df2)
#
#
#
#
#
# #top5 players with highest overal ratings
# print("Final")
# print(df2.iloc[:5])
# df3 = df2.iloc[:5]
#
# bar_plot=(ggplot(df3,aes(x=df3["Name"],y=df3["Best Overall Rating"]))+geom_bar(stat="identity")+labs(title='Player vs Ratings',x='Players',y='Ratings'))
# print(bar_plot)
#
