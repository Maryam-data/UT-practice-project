
# coding: utf-8

# In[36]:


import csv
#open and read file name pybankcsv
with open ('budget_data.csv','r') as pybankcsv:
    csvreader=csv.reader(pybankcsv,delimiter=",")
#Count: The total number of months included in the dataset
#Total: The total net amount of "Profit/Losses" over the entire period
#Average: The average change in "Profit/Losses" between months over the entire period
#greatest_increase: The greatest increase in profits (date and amount) over the entire period
#greatest_decrease: The greatest decrease in losses (date and amount) over the entire period
#poslist is the list of +numbers
#negatie is the list of negative numbers
#MaxMonth is value to hold the greatest increase in profits-date
#MinMonth is value to hold greatest decrease in losses-date
#1 counting number of months and Toatl value:
    next(csvreader)
    Totallist=[]
    Averagelist=[]
    valuelist=[]
    datelist=[]
    minimum=0
    maximun= 0
    count=0
    Total=0
    #looping in data
    for row in csvreader:
        count +=1
        Total += int(row[1])
        
    #make new list from row[1]------------------------------------
        valuelist.append(int(row[1]))
        datelist.append(row[0])
        Totallist=list(zip(valuelist,datelist))
        
    #making Avarage list -------------------------------
    for i in range((len(valuelist)-1)):
        diffrenceValue=int((valuelist[i+1]-valuelist[i]))
        Averagelist.append(diffrenceValue)
    
    #zip lists of columns -------------------------------------
    for i in range(len(Totallist)-1):
        if int(Totallist[i][0])>maximun:
            maximun=int(totallist[i][0])
            greatest_increase=maximun-int(Totallist[i-1][0])
            MaxMonth=Totallist[i][1]
        elif int(Totallist[i][0])<minimum:
            minimum=int(Totallist[i][0])
            greatest_decrease=minimum-int(Totallist[i-1][0])
            MinMonth=Totallist[i][1]
    

  #-----------------------result------------------
 
    print("The total net amount of Profit in the dataset" + ":" + str(Total))
    print("The total number of months included in the dataset"+":" + str(count))
    print("The average change in Profit/Losses" + ":"+  str((sum(Averagelist)/len(Averagelist))))
    print("The greatest increase in profits" + ":" + MaxMonth +  str(greatest_increase))
    print("The greatest decrease in profits" + ":" + MinMonth +  str(greatest_decrease))
    

