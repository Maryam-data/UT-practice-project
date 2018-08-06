
# coding: utf-8

# In[3]:


#-------PYPoll project-------------------------------------------------
#Gole:

#total number of votes cast
# complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

#import csv and os and also from python colloction import counter to count in dictunary
#count=variable to count total number of votes
import csv
import os 
from collections import Counter
#open and read file name pypoll
count=0
percentage=[]
with open ('election_data.csv','r') as pypollcsv:
    csvreader=csv.reader(pypollcsv,delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        count +=1
    print(count)
        


# In[4]:


#read file as dictunary 
pypoll_csv = ('./election_data.csv')
reader = csv.DictReader(open(pypoll_csv))


# In[5]:


#get the list of Candidate as key in dictunary 
candidate_list = [c['Candidate'] for c in reader]


# In[6]:


#COUNT votes for each candidate using dictunarey 
candidate_dict = dict(Counter(candidate_list))


# In[7]:


for i in candidate_dict.values():
    percentage.append(i/sum(candidate_dict.values())*100)


# In[8]:


for name in candidate_dict.keys():
    candidate_dict.get(name)


# In[9]:


# make dictunary from ziping to cadidnate dic keys and percentage list.
candidate_perc_dict = dict(zip(list(candidate_dict.keys()),percentage))
#candinate_vote is dic pof keys and value of candinate ,key
candidate_votes = dict(zip(list(candidate_dict.keys()),candidate_dict.values())) 
winner = list(candidate_votes.keys())[0]


# In[11]:


#Result-----------------------------
print("Election Results")
print("------------------")
print("Total Votes"+" : " + str(count))
for name in candidate_dict.keys():
     print('{} : {:.3f}% ({})'.format(name,candidate_perc_dict.get(name),candidate_votes.get(name)))
print("------------------")
print("Winner: " + winner)


# In[ ]:




