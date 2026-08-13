import pandas as pd
import json
with open("pandas/airports.json",'r') as file:
    data=json.load(file)

print(data.values())


# for airport in data['airports']:  
# # Replace 'airports' with your actual object
# print(data['code'])

# for name in data["airports"]:
#     print(name["name"])

# for city in data["airports"]:
#     print(city["city"] if "US" in data["country"])
# Filter items where the airport country is 'US'
new_list = [x for x in data["airports"] if x.get('country') == 'US']

# print(new_list)
# for item in data["airports"]:
#     if item["country"]=="US":
#         print(item)


# for item in data["airports"]:
#     if item["lon"]>=20.6:
#         print(item)


# for item in data["airports"]:
#     if item["city"]=="Brijing":
#         print(item["name"] , item["country"] , item["city"])
#         print(f'Name: {item["name"]}  Code: {item['code']  }  City: {item["city"]}' )

# for item in data["airports"]:
#     if item.get("country") == "US":
#         print(f"Name: {item['name']} | Code: {item['code']} | City: {item['city']} | Country: {item['country']}")

# Ndata=data[data["airports"],[data["country"]=="US"]]
# print(Ndata)

# for item in data["airports"]:
#     if item.get("country")=="JP":
#         print(f'country: {item["country"]}  code: {item["code"]}  name:{item["name"]}')

# for item in data["airports"]:
#     if item["code"]=="HKG":
#         print(f'Name: {item["name"]} Code:{item["code"]} Lat:{item["lat"]} ')

# df=pd.DataFrame(data)
# print(df.to_string())

# group=df.groupby("country")



# adding a new airport 
# append new dictionary 
new_airport={"code":"LHR","name":"A1 International", "city":"Lahore","country":"PAK", "lat":44.9033, "loc":-83.2273 }
data["airports"].append(new_airport)
air2={"code":"UK","name":"UK International" , "city":"London" ,"country":"ENG",
          "lat":25.23434,"loc":-23.4343}
data["airports"].append(air2)

# print(data["airports"])

air3={"code":"KAR" ,"name":"Karachi International","city":"Karachi" ,"country":"PAK" , "lat":64.3736 ,"loc":-34.5351}
data["airports"].append(air3)
# print(data["airports"])


# country == Pak
# for item in data["airports"]:
#     if item["country"]=="PAK":
#         print(f'name: {item["name"]}  code: {item["code"]}  country: {item["country"]}')

