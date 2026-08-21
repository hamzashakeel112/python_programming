import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

import re
from sklearn.preprocessing import LabelEncoder ,StandardScaler
df = pd.read_csv(r'C:\Users\WB\Documents\Data Science\day5\cleaning\movies.csv')

# printing head
# print(df.head(1))

#  checking the missing values
print(df.isnull().sum())

# checking number of column 
# print(df.shape[0])

# printing the percentage of missing records
# print("--missing record percentage ")
# print((df.isnull().sum()/df.shape[0])*100)

# droping the null values 
df=df.dropna()
# print((df.isnull().sum()/df.shape[0])*100)

# print(df.head(1))

# correcting the Gross

df["Gross"]=df["Gross"].str.replace("$","",regex=False).str.replace("M","").astype(float)



# Converting gross column to original number 
df["Gross"]=df["Gross"]*1000000

print (df["Gross"])

# converting year to start Year
# df['start_year'] = pd.to_numeric(df['YEAR'].astype(str).str.extract(r'\((\d{4})')[0], errors='coerce')

df["Start_Year"]=pd.to_numeric( df["YEAR"].astype(str).str.extract(r'\((\d{4})')[0], errors="coerce" )
df.drop("YEAR", axis=1, inplace=True)



# GENRE
print("GENRE DATA TYPE")
print(df['GENRE'].dtype)
df["Drama"]=df["GENRE"]
try:
    if df["GENRE"].str.contains("Drama"):
        df["Drama"]="DRAMA"
    
    pass
except Exception as e:
    print(e)
# print("DRAMA data type")
# print(df["Drama"].dtype)

print(df["Start_Year"].astype(int))
print(df.info())
print("MOVIE Encoder")
movie_name=LabelEncoder()
df["MOVIES"]=movie_name.fit_transform(df["MOVIES"])
# print(df["MOVIES"])

# genre_encoder
genre_name=LabelEncoder()
df["GENRE"]=genre_name.fit_transform(df["GENRE"])
# print(df["GENRE"])

# oneLine encoding
one_line=LabelEncoder()
df["ONE-LINE"]=one_line.fit_transform(df["ONE-LINE"])
# print(df["ONE-LINE"])

# STARS
star_encoding=LabelEncoder()
df["STARS"]=star_encoding.fit_transform(df['STARS'])
print(df)