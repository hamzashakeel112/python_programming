import numpy as np
import pandas as pd
import re

data1 = pd.read_csv(r'C:\Users\WB\Documents\Data Science\day5\cleaning\movies.csv')

# print(data1.dropna().count())
# print(data1.drop_duplicates())
data1=data1.drop_duplicates() #removing the duplicate

# removing the null rows
data1=data1.dropna()
# then removing the column
data1=data1.dropna(axis=1)

# print(data1.columns)
# 1. Extract the 4-digit start year from the YEAR column
data1['start_year'] = pd.to_numeric(data1['YEAR'].astype(str).str.extract(r'\((\d{4})')[0], errors='coerce')

# 2. Sort from Newest to Oldest (Descending)
df_sorted_newest = data1.sort_values(by='start_year', ascending=False)

# Display top 10 newest movies
# print(df_sorted_newest[['MOVIES', 'start_year', 'RATING']].head(10))


try:
    data1["start_year"]=pd.to_numeric(data1["YEAR"].astype(str).str.extract(r'\((\d{4}'))
except Exception as e:
    pass
    
# print(data1["start_year"])


# Movie every year

# data1["start_year"]=pd.to_numeric(data1["YEAR"].astype(str).str.extract(r'\((\d{4}')[0],errors="coerce")
data1['start_year'] = pd.to_numeric(data1['YEAR'].astype(str).str.extract(r'\((\d{4})')[0], errors='coerce')
movie_per_year=data1.groupby("start_year")["MOVIES"].count().reset_index()


movie_per_year.columns=["Release Year", "MOVIE NAME"]
print(movie_per_year)


#Rating  
# print(data1["RATING"].dtype )



top_movie=data1[data1["RATING"]<9.0 ]
print(top_movie[["RATING","MOVIES"]])



top_rate=data1[data1["RATING"]>8.2]
# print(top_rate.dropna())
# row=top_rate



# most_votes=data1[data1["VOTES"]>30000]
# print(most_votes)
# data1["VOTES"]=data1["VOTES"].astype(int)
# print(data1["VOTES"].dtype)



# data1["POST"] = data1["VOTES"].astype("Int64")
# Clean commas and convert to float (double)
data1["VOTES"] = data1["VOTES"].str.replace(",", "").astype(int)
# print(data1["VOTES"])



# type conversion 
high_v=data1[data1["VOTES"]>600000]
print(high_v[["VOTES","MOVIES"]])

genre=data1["GENRE"].str.replace(","," ").replace("\n","")


# top_horer=data1[(data1[data1["VOTES"]>600000])&(data1[data1["GENRE"].str.contains("Drama")])]
# Fixed: Combine conditions inside data1[...]

print("--TOP--RATINGS")
top_rate = data1[(data1["VOTES"] > 600000) & (data1["GENRE"].str.contains("Drama", na=False)) &(data1["RATING"]>=8.2)]
top_rate.sort_values(by="start_year",ascending=False)
print(top_rate[["VOTES","MOVIES","RATING","start_year"]])


print("movie after 2010")
# print(data1["start_year"].dtype)
movie_2010=data1[(data1["start_year"]>2010 )& (data1["start_year"]<2015)]
print(movie_2010)


print("--late 19s movies earn more then 2M ")
data1["Gross"]=pd.to_numeric(data1["Gross"].astype(str).str.replace("$","",regex=False).str.replace("M","",regex=False)) *1000000
# convert it into float now

movie_profit=data1[(data1["Gross"]>2000000)&(data1["RATING"]>8.2)&(data1["start_year"]<2000)]
print(movie_profit)


# most gross every year 
# top_year=data1["start_year"].groupby("year_start")["Gross"].max()

# print(top_year.min())
# print(top_year)


# 1. Group the DataFrame by start_year and find max Gross per year
# Sort by Gross descending and keep the top movie for each start_year
top_year = (
    data1.sort_values(by="Gross", ascending=False)
    .drop_duplicates(subset=["start_year"])
    [["start_year", "MOVIES", "Gross"]]
    .sort_values(by="start_year")
    .reset_index(drop=True)
)

print(top_year)

# 2. Print results
print("Lowest among the top grossing movies:", top_year.min())
print(top_year[["start_year","Gross","MOVIES"]])

# for i in data1["start_year"]:
    

#     print(i)

# for i in range(data1["start_year"].min(),data1["start_year"].max()):
#     try:
#         if data1["start_year"]==i:

#             # if data1["start_year"]:
#             #     print

#             print(f'{data1["MOVIES"]} is top sell of year{i}')
#     except Exception as e:
#         print(e)

