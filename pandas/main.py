import pandas as pd
# creating a series 
# data=[100,200,300]
# series= pd.Series(data)
# print(series)
# add index in data 




# changing indexing in a series
data= [100,200,300]


series=pd.Series(data, index=["a","b","c"])




# searching with location in series by label (loc[]) and updating values 
series.loc["c"]=1122
# print(series)
print(series.iloc[3])

# apply condition 
# print(series[series>=200])


calories={"day1":1700,"day2":1800,"day3":1900}
series2=pd.Series(calories)
# calories["day2"]+=500
# print(calories)




team={
    "Name":["john","Doe","peter"],
    "Age":[30,40,50]
}
df=pd.DataFrame(team)
# print(df.loc[1])
# print(df.iloc[1])

# add new column 
df["Job"]=["cook","N/A","Cahshier"]
# print(df)

new_row=pd.DataFrame([{"Name":"jack","Age":49,"Job":"Cashier"}])
df=pd.concat([df,new_row])
print(df[df["Age"]<50])
