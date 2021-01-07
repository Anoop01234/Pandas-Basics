#importing pandas package
>> import pandas as pd

#Reading CSV file
>> file= pd.read_csv("sample.csv")

# Reading particular sheet of an excel file
>>file1= pd.read_excel("sample.xlsx","sheet1")

# Writing content of dataframe to csv file
>> file.to_csv("sample2.csv")

# Writing content of data frame to excel file
>> file1.to_excel("sample3.xlsx","sheet3")

# Looking at the top n records
>> sample.head(20)

# Looking at the bottom n records
>> sample.tail(30)

# Viewing the column names
>> sample.rows

# Viewing the row names
>> sample.rows

# Renaming the column/row name will create new data frame
>> a= sample.rename(column={"OldColumnName","NewColumnName"})

# To reaname the column of existing data frame use inplace= True, like:
>> a= sample.rename(columns={"OldCOlumnName","NewColumnName"}, inplace =True)

# Selecting Column or rows
>> Sample["Column1","Column2"]

#Filtering out the records
>> sample[sample["column1"]>300]
>> sample[sample["column1"]>250 or sample["column2"]==40] 
>> sample[sample["column1"]>400 and sample["column2"]==50]

#Aggregation of data

# Groupby by applying sum function
sample.groupby("column1").sum()

# Groupby by applying count function
sample.groupby("column1","column2").count()

# Pivot table
#the following shows count
pd.pivot_table(d,values="column1",index=["column2","column3"],column=["column4"].aggfunc=len)

# Cross Tab
pd.crosstab(sample.column1,sample.column2)

# Merging 
# The how mentioned can be inner, outer, left or right based on the requirement
pd.merge(sample1,sample2,on="column1",how="inner")

# Concatinating
pd.concat(sample1,sample2)

# Applying functions

# Using map function
sample["column1"].maps(lambda x: 20 + x) # This will add 20 to each element of column1

# Using apply function
sample["column1","column2"].apply(sum) # This will return sum of all values of column1 and column2

# Using applymap
f=lambda x: x + 30
sample.applymap(f) # This will add 30 to each element of the dataframe

# Finding unique values
sample["column1"].unique()

# Returning quick stats (like mean, std, min, max, etc)
sample.describe()

# Finding covariance
sample.cov()

# Finding correlation
sample.corr()
