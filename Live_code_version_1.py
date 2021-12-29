pip install psycopg2

import pandas as pd
import psycopg2
con=psycopg2.connect(host="localhost",
                     database="Trainning",
                    user="postgres",
                    password="",
                    port=5432)

df1=pd.read_sql("select * from transaction_history",con)
print(df1)

#Try different character functions used in daily life

#upcase first letter of the string
df1['merchant_name']=df1['merchant_name'].str.capitalize()

#Conversts string into lower case
df1['transaction_segment']=df1['transaction_segment'].str.casefold()
df1['transaction_segment']=df1['transaction_segment'].str.lower()

#Conversts string into lower case
df1['transaction_segment']=df1['transaction_segment'].str.upper()

#Calculate the number of colums without missing values in it
df1.count(axis='columns')

#Calcuate the number of rows without missing values in it
df1.count(axis='rows')

#calculate the count for each variable excluding missing values
#df1.set_index(['credit_card_id','transaction_segment']).count(level='credit_card_id')

#replace characters in a string
df1['merchant_name']=df1['merchant_name'].str.replace('1','b')

#Find position of a string
print(df1['merchant_name'].str.rfind("gos"))



#loops in lists
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i+=1

#conditions and comprehension in lists

newlist = []

for x in thislist:
    if 'a' in x:
        newlist.append(x)

#first character of the items in list to upper case
for x in range(len(newlist)):
    newlist[x]=newlist[x].capitalize()
print(newlist)


#replace item in list open(not resolved)
# for x in range(len(thislist)):
#     if x=='banana':
#         thislist[x]='hello'
        
# print(thislist)

#append to a list
for x in thislist:
    newlist.append(x)

print(newlist)

#condition in a list
for x in range(len(newlist)):
    if x <=3:
        newlist1=newlist[:x]


print(newlist1)