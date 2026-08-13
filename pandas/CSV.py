import pandas as pd
# df=pd.read_csv("pandas/data.csv")
# print(df.loc[1:50,["Name","Height"]].to_string()) 
# print(df.loc[1:90,["Height","Name"]].to_string())
# 



# ask from the user about the pokemon 
# df=pd.read_csv("pandas/data.csv",index_col="Name")
# pokemon= input("enter name")
# try:
#     print(df.loc[pokemon])
# except:
#     print(f"{pokemon} dont exist")




# filtering the data
df=pd.read_csv("pandas/data.csv")
# tall=df[df["Height"]>=2]
# print(tall)

weight=df[df["Weight"]>=60]
# print(weight.to_string())
type1=df[(df["Height"]>=3) & (df["Type1"]=="Water")]
type2=df[(df["Type1"=="Dragon"])&(df["Type1"]=="Psychic")]
# print(type1)

# print(df.mean(numeric_only=True))
# group=df.groupby("Type1")
# print(group["Height"].sum())

print(df.drop(columns=["Legendary"]))
# print(df.dropna(subset=["Type2"]).to_string())