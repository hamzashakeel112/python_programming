import pandas as pd
import pandas as pd

# Hardcode the path so Python finds it regardless of current folder
file_path = r'C:\Users\WB\Documents\Data Science\Day3\Pandas operation\na-isal-year-ended-march-2025-sector-accounts.csv'

data_frame = pd.read_csv(file_path)
# print(data_frame.head())
# print(data_frame.to_string())

# print the column name 
# print(data_frame.columns)

# summary
# print(data_frame.info())


# find missing value ture mean null false mean not null
# print(data_frame.isnull())

#  sum of not null values
# print(data_frame.isnull().sum())

# removing missiong values
# dropna remove the row that has atleast one valeue missing
# print(data_frame.dropna())

# adding axis in parameter will reove that column in dataframe 
# print(data_frame.dropna(axis=1))


# data_frame["new col"]=1
# print(data_frame.head())


# sort Data Frame

# print(data_frame.sort_values(by='Series_title_4',ascending=False))

# we can also sort by multiple columns 
# print(data_frame.sort_values(by=['Series_title_4',"Data_value"]).head(10))


# filter key word 
# parameters
# items: a list of label to keep 
# like: match a substring 
# regex: expression label that match labels 
# axis :specific wither to filter by row(axis=0), or by column (axie=1)

# print(data_frame.filter(like='' ,axis=1))


# by=data_frame.groupby([ "Series_title_5"]).agg(total_mag=("Magnitude"))
# print(by.head(30))
sector_tools=data_frame.groupby("Series_title_4")[["Data_value","Magnitude"]].sum()

# print(sector_tools)




# always clean dataset first
# using dropna
# df_clean = data_frame.dropna().sum()
# print(df_clean)


# Calculate total rows drop
# rows_before = len(data_frame)
# df_clean = data_frame.dropna()
# rows_after = len(df_clean)

# dropped_rows = rows_before - rows_after
# print(f"Total rows dropped: {dropped_rows}")


# data_frame['Series_title_5'] = data_frame['Series_title_5'].fillna("Unknown")
# print(data_frame.tail(40))


# fill specific cell
# data_frame.loc[20131, "Series_title_5"] = "KNOWN"
# print(data_frame.tail(10))

# counting not null value in using isna().sum()
# print(data_frame["Series_title_5"].isna().sum())
# print(data_frame["STATUS"].isna().sum())
# with using loc we can replace any value at any row(row must be defined)

# dropna fillna loc isna 
# df['column'].fillna(0)


# filtering the data 
# filter_data=data_frame["Data_value"]<3000
# print(filter_data.count)
# print(data_frame)


# Multiple Filter 
# filter_data = (data_frame["STATUS"] == "REVISED") & (
#     data_frame["Units"] == "Dollars"
# )
# # 2. Apply the mask to the DataFrame and view the top 20 rows
# filtered_df = data_frame[filter_data]
# print(filter_data.head(20))


# filterD=(data_frame["Series_title_3"]=="Market") &(data_frame["Series_title_5"]=="National private and foreign control")

# filtered_data=data_frame[filterD]
# print(filtered_data)

filter=(data_frame["Series_title_4"]=="Households") & (data_frame["Series_title_5"]=="National private control")
# filtered_data=data_frame[filter]
# print(filtered_data)

# how to drop the duplicate row 
# drop_duplicate()
print(len(data_frame.drop_duplicates())-len(data_frame.count()))
print(len(data_frame.drop_duplicates().count()))
print(len(data_frame))



# aggrigate in pandas 
# .maen() .sum() .count()
# filterdata=data_frame["Series_title_4"]=="Households"
# print(filterdata.count())




df1 = pd.DataFrame(
    {
        "Sector": [
            "Central government institutions",
            "Corporate business enterprises",
            "Privare bussiness institute"
        ],
        "Total_Date_Value": [133462.0,562320.0,200209.0]
    }
)
# print(df1)
df2=pd.DataFrame(
    {
        "Sector":["Central government institutions","Corporate business enterprises",],
        "Economic_Group":["Public Sector","Private Sector"],
        "Risk_Rating":["Very Low", "Medium"]

    }
)

# df_merge=pd.merge(df1,df2,left_on="Sector",right_on="Sector", how="inner")
# print(df_merge)

# df_merge=pd.merge(df1,df2.left_on,right_on,how)
# df_merge=pd.merge(1st dict , 2nd dict, left_on,right_on.how=)

data_frame=data_frame.dropna()
data_frame=data_frame.drop_duplicates()
# data_frame=data_frame[data_frame["Series_title_4"]=="House"]
# i=0
# while(i<len(data_frame)):
#     if data_frame["Series_title_4"]=="Households":
#         data_frame["Series_title_4"]="HOUSEHOLDS"
#     i+=1


data_frame["Series_title_5"]=data_frame["Series_title_5"].replace("All control","ALL CONTROL")
print(data_frame)