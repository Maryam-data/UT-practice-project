
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# #### Read file and explore the data 

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
file_to_load = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# #### Player Count

# * Display the total number of players
# 

# In[2]:


Total_Players= len(purchase_data["SN"].value_counts())

Total=pd.DataFrame({"Total_player":[Total_Players]})
Total.head()


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[4]:


Unique_Items= len(purchase_data["Item ID"].value_counts())
Average_Price= str(round(purchase_data["Price"].mean(), 2))
Number_Purchases=purchase_data["Purchase ID"].count()
Total_Revenue=purchase_data["Price"].sum()
#print(Unique_Items , Average_Price, Number_Purchases,Total_Revenue)
Purchasing_Analysis= pd.DataFrame({"Number of Unique Items":[Unique_Items],"Average Price":[Average_Price],
                                   "Number of Purchases":[Number_Purchases],"Total Revenue":[Total_Revenue]})
Purchasing_Analysis.head()
                                


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[5]:


Gender_Demographics = purchase_data["Gender"]

Gender= pd.DataFrame(Gender_Demographics.value_counts())
Gender["Percentage of Players"]=round(100* (Gender["Gender"]/Total_Players),2)
Gender=Gender.rename(columns={"Gender" : "Total Count"})

Gender.head()


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[7]:


Analysis_Gender= purchase_data.groupby("Gender")

Gender["Avg Purchase Total per Person"]= round(Analysis_Gender["Price"].mean(),2)
Gender["Total Purchase Value"]= Analysis_Gender["Price"].sum()
Gender["Purchase Count"]= Analysis_Gender["Purchase ID"].count()
Gender["Average Purchase Price"]= round(Analysis_Gender["Price"].mean(),2)


Gender["Avg Purchase Total per Person"]=round(Analysis_Gender["Price"].mean(),2)
Gender.head()


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[8]:


# Establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
purchase_data["Age_group"]= pd.cut(purchase_data["Age"],age_bins ,labels = group_names)
Age_Demographics= purchase_data.groupby("Age_group").count()
Age_Demographics["Percentage of Players"]=round(100* (Age_Demographics["Age"]/Total_Players),2)
Age_Demographics = Age_Demographics[["Percentage of Players", "Price"]]
Age_Demographics=Age_Demographics.rename(columns={"Price" : "Total Count"})
Age_Demographics.head()


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[9]:


age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
purchase_data["Age_group"]= pd.cut(purchase_data["Age"],age_bins ,labels = group_names)
newpurchase_data=purchase_data.groupby("Age_group")
Average_Purchase =round(newpurchase_data["Price"].mean(),2).map("${:.2f}".format)   #map("${:.2f}".format)
Total_Value=newpurchase_data["Price"].sum(). map("${:.2f}".format)
Purchase_Count=newpurchase_data["Purchase ID"].count()
Purchase_Count
Purchasing_Analysis= pd.DataFrame(Purchase_Count)
Purchasing_Analysis["Average Purchase Price"]=Average_Purchase
Purchasing_Analysis["Average Purchase Total per Person"]=Average_Purchase
Purchasing_Analysis["Total Purchase Value"]=Total_Value
Purchasing_Analysis=Purchasing_Analysis.rename(columns={"Purchase ID" : "Purchase Count"})
Purchasing_Analysis.head()


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[10]:


Top_Spenders=purchase_data.groupby("SN")
Average_Purchase =round(Top_Spenders["Price"].mean(),2).map("${:.2f}".format) 
Total_Value=Top_Spenders["Price"].sum(). map("${:.2f}".format)
Purchase_Count=Top_Spenders["Purchase ID"].count()
#Purchase_Count
Purchasing_Analysis= pd.DataFrame(Purchase_Count)
#Purchasing_Analysis.head()
Purchasing_Analysis["Average Purchase Price"]=Average_Purchase
#Purchasing_Analysis["Average Purchase Total per Person"]=Average_Purchase
Purchasing_Analysis["Total Purchase Value"]=Total_Value
Purchasing_Analysis=Purchasing_Analysis.rename(columns={"Purchase ID" : "Purchase Count"})
Purchasing_Analysis.sort_values("Purchase Count", ascending=False).head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[11]:


Most_Popular= purchase_data.groupby(["Item ID", "Item Name"])
Total_Value= Most_Popular["Price"].sum().map("${:.2f}".format)
Average_Purchase =round(Most_Popular["Price"].mean(),2).map("${:.2f}".format)   #map("${:.2f}".format)
Purchase_Count= Most_Popular["Purchase ID"].count()
MostPopular_Analysis= pd.DataFrame(Purchase_Count)
MostPopular_Analysis["Total Purchase Value"]=Total_Value
MostPopular_Analysis["item price"]= Average_Purchase

MostPopular_Analysis.head()
MostPopular_Analysis=MostPopular_Analysis.rename(columns={"Purchase ID" : "Purchase Count"})
MostPopular_Analysis.sort_values("Purchase Count", ascending=False).head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[13]:


Most_Popular= purchase_data.groupby(["Item ID", "Item Name"])
Total_Value= Most_Popular["Price"].sum()#.map("${:.2f}".format)
Average_Purchase =round(Most_Popular["Price"].mean(),2).map("${:.2f}".format)   #map("${:.2f}".format)
Purchase_Count= Most_Popular["Purchase ID"].count()
MostPopular_Analysis= pd.DataFrame(Purchase_Count)
MostPopular_Analysis["Total Purchase Value"]=Total_Value
MostPopular_Analysis["item price"]= Average_Purchase

MostPopular_Analysis.head()
MostPopular_Analysis=MostPopular_Analysis.rename(columns={"Purchase ID" : "Purchase Count"})
#MostPopular_Analysis.sort_values("Total Purchase Value", ascending=False).head()
MostPopular_sorted= MostPopular_Analysis.sort_values("Total Purchase Value", ascending=False).head()
MostPopular_sorted["Total Purchase Value"]=MostPopular_sorted["Total Purchase Value"].map("${:.2f}".format)
MostPopular_sorted.head()

