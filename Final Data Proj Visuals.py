import pandas as pd

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

import os

##get current operating system
print(os.getcwd())

##redirect to the working directory
print(os.chdir(r"C:\Users\ruthk\Data Analytics for Business Project"))

##reading the csv file
travel_data = pd.read_csv("travel.csv")

## datafram as travel. csv
df = pd.read_csv("travel.csv")

##printing out the top of the data.
print(travel_data.head())

##MATPLOTLIB Graph

##Matplotlib graph to show the ages, salaries of designation to see what age group and position to target.
plt.style.use("fivethirtyeight")

ages_x = [20,30,40,50,60]

avp_y = [17705, 29275, 32504,35284,37502]

plt.plot(ages_x, avp_y, marker = "4", linestyle = "-", color = "b", label ="AVP")

exc_y = [16009, 17559, 21614, 34187, 98678]

plt.plot(ages_x, exc_y, marker = "2", linestyle = "--", color = "k", label ="EXC")

man_y = [4678, 19762, 20237,25218,38525]

plt.plot(ages_x, man_y, marker = "3", linestyle = "--", color = "r", label ="MAN")

sman_y = [17372,24434,25976,29003,38395]

plt.plot(ages_x, sman_y, marker = "v",  color = "y",label ="SMAN")

plt.plot(ages_x, avp_y, marker = "o", linestyle = "--", color = "g",  label ="VP")

plt.xlabel("Ages")
plt.ylabel("Monthly Income")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()

##SEABORN GRAPH

##Showing  bar chart of Monthly income if Single through to Ummarried for both Males & Females again to see who has money.
ax = sns.barplot(y=  "MaritalStatus" , x = "MonthlyIncome" , data=travel_data, ci=None, hue = "Gender", orient="h",color="blue")
plt.show()


##BOXPLOT
##To see the people to target to go on holidays, from their income, marital status & Occupation.
sns.set(rc={"figure.figsize":(12,10)})
sns.catplot(y="MonthlyIncome", x ="MaritalStatus", col = "Occupation",data=travel_data  , kind="box")
plt.show()

