import pandas as pd

import pandas as pd

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

import os

##get current operating system
from Tools.scripts.dutree import display

print(os.getcwd())

##redirect to the working directory
print(os.chdir(r"C:\Users\ruthk\Data Analytics for Business Project"))

##reading the csv file
travel_data = pd.read_csv("travel.csv")

## datafram as travel. csv
df = pd.read_csv("travel.csv")

##printing out the top of the data.
print(travel_data.head())

## Check the heading on the file
print(travel_data.columns)

##Check data types
print(travel_data.dtypes)

##Check the shape of the ds.
print(travel_data.shape)

##Check for primary keys
print(travel_data.CustomerID.unique())

##Lenght of ds to see if there is any duplicate.
print(len(travel_data.CustomerID.unique()))

##Types of Occupations people have.
print(travel_data['Occupation'].value_counts().head())

## Types of contacts, whether it was self or business inquiry.
print(travel_data["TypeofContact"])

##People with the same Monthly Income.
print(travel_data['MonthlyIncome'].value_counts().head(20))

##USING THE "&" AND "|" VALUES

##print out ds of ages who is greater than or equal to 35 AND income in greater than or equal to 50K
print(travel_data[(travel_data["Age"] >= 35) & (travel_data["MonthlyIncome"] >= 50000)].head())

##print out ds of ages who is greater than or equal to 35 OR are less than or equal to 60
print(travel_data[(travel_data["Age"] >= 35) | (travel_data["Age"] <= 60)].head())

##reading the csv file
travel_data = pd.read_csv("travel.csv")

## datafram as travel. csv
df = pd.read_csv("travel.csv")

##INDEXING##

##Changing Customer Id to the index column
df = pd.read_csv("travel.csv", index_col="CustomerID")
print(df.head())

##Resetting 0-end to the index column
df.reset_index(inplace=True)
print(df.head())

##Changing Customer Id to the index column.
df = pd.read_csv("travel.csv", index_col="CustomerID")
print(df.head())

##Sorting the datafame from the index.
print(df.sort_index())

##SORTING##

##Sorting Age Value in acending order.
print(df["Age"].sort_values().head(50))

##Sorting Age & Monthly Income in decending & ascending order.
df.sort_values(by=["Age", "MonthlyIncome"], ascending=[False, True], inplace=True)
print(df.head())

##Sorting the 10 largest Monthly Income
print(df["MonthlyIncome"].nlargest(10))

##Grouping##

##Grouping the people with positions and there average monthly income.
print(df.groupby("Designation").MonthlyIncome.mean().head(10))

##Grouping the Types of contacts,positions, gender and there total,average, max & min monthly income.
print(df.groupby(["TypeofContact", "Designation", "Gender"]).MonthlyIncome.agg(["sum", "mean", "max", "min"]).head(20))

##REPLACE MISSING VALUES

##Replacing the blank values with Nan
travel = pd.read_csv("travel.csv", na_values="NaN")
print(travel_data.head(20))

##DROPPING VALUES##


##dropping rows that contain null values
droprows = travel_data.dropna()
print(travel_data.shape, droprows.shape)

##Checking how many rows that have missing values & in what catagories
missing_values_count = travel_data.isnull().sum()
assert isinstance(missing_values_count, object)
print(missing_values_count)

##Filling in missing values with zero
cleaned_data  =travel_data.fillna(0)
cleaned_data.isnull().sum()
print(cleaned_data.isnull().sum())

##Checking if the rows is missing values False = Missing values, True = No missing values
print(df.isnull().any())

##Drop columns CityTier,PitchSatisfactionScore.
travel_data.drop(["CityTier", "PitchSatisfactionScore"], axis=1, inplace=True)
print(travel_data.columns)

##Drop duplications from the Customer ID as thats the only place there would be dup relevent.
drop_duplicates = travel_data.drop_duplicates(subset=['CustomerID'])
print(travel_data.shape, drop_duplicates.shape)
##From the results in the console it looks like there are no duplication as per the Customer ID


##ITERROWS

##Returns the index columns
for i in df: print (i)

##Returns the index, age & monthly Income rows of data
for i, row in df.iterrows():
    print(i, row[0],row[1],row[2],)


##MERGING DATAFRAMES
##I didnt have any DF to merge, so I have just put one in.
df1 = pd.DataFrame({"city": ["Dublin", "Galway", "Cork"],
                           "hotels":["Westbury", "G", "Savoy"],})
df1

df2 = pd.DataFrame({"city": ["Dublin", "Galway", "Cork"],
                           "rivers":["Liffey", "Corribe", "Lee"],})
df2

df3 = pd.merge(df1, df2, on = "city")
df3

print(df3)

##LISTS##

##List of all the headings of the columns
list1 = ["CustomerID" ,"ProdTaken","Age", "TypeofContact", "CityTier", "DurationOfPitch", "Occupation", "Gender", "NumberOfPersonVisiting"," NumberOfFollowups",
"ProductPitched","PreferredPropertyStar", "MaritalStatus", "NumberOfTrips", "Passport", "PitchSatisfactionScore", "OwnCar", "NumberOfChildrenVisiting",
"Designation", "MonthlyIncome"]
print(list1)

#array1 = np.array(list1)
#print(type(array1))


##Lenght of the list
print(len(list1))

##Just listing the first columns of the df
print(list1[:2])

##Showing the 2nd last heading on the list ie Designation
print(list1[-2])

##Adding the header/column name "Hotels"
list1.insert(20, "Hotels")
print(list1)

#Slicing the list, removing Hotels
print(list1[:20])

##Removing Occupation from the list.
list1.remove("Occupation")
print(list1)


##NUMPY##

##Array is the Monthly Income & Designation
x=np.array(df["MonthlyIncome"])
y=np.array(df.iloc[:, :19])
print(x)
print(y)

##Datafaram & Print list
list1 = ["CustomerID" ,"ProdTaken","Age", "TypeofContact", "CityTier", "DurationOfPitch", "Occupation", "Gender", "NumberOfPersonVisiting"," NumberOfFollowups",
"ProductPitched","PreferredPropertyStar", "MaritalStatus", "NumberOfTrips", "Passport", "PitchSatisfactionScore", "OwnCar", "NumberOfChildrenVisiting",
"Occupation", "Gender",]
print(type(list1))

df = pd.read_csv("travel.csv")
print(df)

np_array = df.to_numpy()
print(np.array)

print(df[["Age", "MonthlyIncome"]].to_numpy())


##Print type array ie Numpy
array1 = np.array(list1)
print(type(array1))

##Dataframe to use for Numpy
data = {"CustomerID":[200000,200001,200002,200003],
"Age":[41,49,37,33],
"Occupation":["Salaried","Salaried","Free Lancer","Salaried"],
"Gender":["Female","Male","Male","Female"],
"MonthlyIncome":[20993,20130,17090,17909]}
df = pd.DataFrame(data)
print(df)

##Convert DF to Numpy Array
np_array = df.to_numpy()
print(np.array)

##Converting colums to Numpy Array.
print(df[["Age","MonthlyIncome","Gender"]].to_numpy)


##FUNCTIONS - Reusable Functions##


#Average/Mean of column
print("Mean for column:", travel_data["MonthlyIncome"].mean())

#Average of column column
a= int(input("first age"))
b= int(input("first age"))
c=int(input("first age"))
add = a+b+c
print("addition is", add)
average=add/3
print("Average =",average)
