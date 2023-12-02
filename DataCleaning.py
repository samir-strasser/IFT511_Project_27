# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:00:31 2023

@author: samir
"""

import pandas as pd
dat = pd.read_csv('School Data.csv')
print("PART ONE++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print('Shape',dat.shape)
'''
for c in dat.columns: 
     print( c, dat[c].isnull().sum() )
'''
#I want to drop the cols with the most missing data. First going for ones over 100
toDrop = ['Offers Electives?','Sports Rank','Mental Health Services?','Math Score',\
                 'English Score','Suicide Data',\
                 'Crime-related Data','Lunch%-Free','Lunch%-Reduced',\
                     'Lunch%-Paid','Unnamed: 27','Teaching/Educational Method']

print("Deleted Every Column with missing values over 95")
for i in range(0,len(toDrop)):
    dat = dat.drop(toDrop[i],axis=1)
print('New Shape',dat.shape)
'''
for c in dat.columns: 
     print( c, dat[c].isnull().sum() )
'''

print("Dropping all rows with empty values")
dat = dat.dropna()
print('New Shape',dat.shape)

print("PART TWO++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
dat = dat.drop_duplicates(subset=['School Name', 'Zip Code'])
print("Removed Duplicates if they had the same name/zipcode")
print('New Shape',dat.shape)
print("PART THREE++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
dat['2022 Student Enrollments'] = pd.to_numeric(dat['2022 Student Enrollments'],\
                                                errors='coerce')
dat = dat.dropna()
print("I made the [2022 Student Enrollment] part numeric and dropped all rows",\
      "that could not be converted as some had things like 'cant find'")
print('New Shape',dat.shape)

print("")
dat['National Rank'] = pd.to_numeric(dat['National Rank'],\
                                                errors='coerce')
dat = dat.dropna()
print("I made the [National Rank] part numeric and dropped all rows",\
      "that could not be converted as some had things like 'Unranked'")
print('New Shape',dat.shape)
print("")
dat['AZ Rank'] = pd.to_numeric(dat['AZ Rank'],\
                                                errors='coerce')
dat = dat.dropna()
print("I made the [AZ Rank] part numeric and dropped all rows",\
      "that could not be converted as some had things like 'Unranked'")
print('New Shape',dat.shape)

racialL = ['Racial%-White','Racial%-Black','Racial%-Native','Racial%-Hispanic',\
           'Racial%-Asian','Racial%-Other']
print("")
for n in racialL:
    dat[n] = dat[n].str.replace('%','')
    dat[n] = pd.to_numeric(dat[n],\
                           errors='coerce')
dat = dat.dropna()
print("I made the [Racial%-XXXXX] parts numeric and dropped all rows",\
      "that could not be converted as some had things like 'Not Found'")
print('New Shape',dat.shape)

print("")
print("Next I get rid of ', AZ' and similar strings in the City tab as we",\
      " know all data is in arizona. Size does not change ")
dat['City'] = dat['City'].str.replace(', AZ','')
dat['City'] = dat['City'].str.replace(',AZ','')
dat['City'] = dat['City'].str.replace(', Arizona','')
print("")
print("Now I want to clean the YES and NO columns. First I need to make all Y/N's the same")
a = dat['AP Classes?'].value_counts()
print("For example this is what the column [AP Classes?] looks like if we value count it\n",a)
WaysOfYes = ['Yes','yes','YES','Yes ','Y ','YEs','AP CLASSES - AP CLASSES - Yes',\
             'Dual Enrollment - Dual Enrollment - Yes']
WaysOfNo = ['No','NO','no']

for y in WaysOfYes:
    dat['AP Classes?'] = dat['AP Classes?'].str.replace(y,'AP CLASSES - Yes')
    dat['Dual Enrollment?'] = dat['Dual Enrollment?'].str.replace(y,'Dual Enrollment - Yes')
    dat['Offers Sports?'] = dat['Offers Sports?'].str.replace(y,'Offers Sports - Yes')
for n in WaysOfNo:
    dat['AP Classes?'] = dat['AP Classes?'].str.replace(n,'AP Classes - No')
    dat['Dual Enrollment?'] = dat['Dual Enrollment?'].str.replace(n,'Dual Enrollment - No')
    dat['Offers Sports?'] = dat['Offers Sports?'].str.replace(n,'Offers Sports - No')
    
a = dat['AP Classes?'].value_counts()
print("Now it looks like\n",a)
print("I WILL DO THIS FOR ALL Y/N FEATURES BUT WILL NOT SHOW IT ALL :)")

v = dat['Student-Teacher Ratio'].value_counts()
print("\nLooking at the [Student-Teacher ratio] there are 27 missing values.")
print("At this point that is more than a 5th of our data, therefore I think it is")
print("better if we just drop the column")
dat = dat.drop('Student-Teacher Ratio',axis=1)
print('New Shape',dat.shape)

dat = dat.reset_index()
dat = dat.drop("index",axis=1)

dat['City'] = dat['City'].str.upper()
print("\nI also made the city column all uppercase so that when I divide them up")
print("catagorically the names are consitant")
#Making the new data
print("\nNow I am making the new data First we add the ratio values")
newDat = dat[["2022 Student Enrollments","National Rank","AZ Rank",'Racial%-White','Racial%-Black','Racial%-Native','Racial%-Hispanic',\
           'Racial%-Asian','Racial%-Other']]

print("New Data shape",newDat.shape)
cat = ['School Name','City','AP Classes?','Dual Enrollment?','Offers Sports?']
for c in cat :
    newDat = pd.concat([newDat,pd.get_dummies(dat[c])],axis=1)

print("\nNow sorting all of the catagorical comlumns")
print("New Data shape",newDat.shape)





