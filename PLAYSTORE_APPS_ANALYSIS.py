#!/usr/bin/env python
# coding: utf-8

# # PLAY STORE APPS ANALYSIS AND VISUALIZATION

# ### About the project:
# 
# In this project, I'd be will be working on a real-world dataset of the google play store, one of the most used applications for downloading android apps. This project aims on cleaning the dataset, analyze the given dataset, and mining informational quality insights. This project also involves visualizing the data to better and easily understand trends and different categories.
# 
# ### Project Description: 
# 
# This project will help one understand how a real-world database is analyzed using SQL, how to get maximum available insights from the dataset, pre-process the data using python for a better upcoming performance, how a structured query language helps us retrieve useful information from the database, and visualize the data with the power bi tool.
# The Project will consist of 2 modules:
# 
# - Module 1: Pre-processing, Analyzing data using Python and SQL.
# - Module 2: Visualizing data using Power bi.

# ## Module 1 : Pre-processing, Analyzing data using Python and SQL
# 
# The first step of this analysis would involve pre-processing the data using python libraries. After this pre-processing also known as data cleaning, the cleaned data would then be further analyzed using MySQL to garner insights based on our reserach question.

# ## Task 1 : Pre-processing the data

# In[1]:


# Firstly, we would have to import all the necessary libraries to be utilized

import pandas as pd
import numpy as np
from numpy import nan
from datetime import datetime, timedelta


# In[2]:


#There are two datasets which we would then import using pandas
apps = pd.read_csv("playstore_apps.csv", index_col = 'App')
reviews = pd.read_csv("playstore_reviews.csv", index_col = 'App')


# In[3]:


#Lets see the column attributes for apps dataset
apps.info()


# In[4]:


# Let's find the no of rows and columns in apps dataset
apps.shape


# In[5]:


# Let's view the first 5 rows of the apps dataset
apps.head()


# In[6]:


apps.duplicated().value_counts()


# ### Findings on `apps` dataset
# 
# 1. Data contains 10841 rows and 12 columns 
# 2. When importing the datasets the `App` column was used as the index column.
# 3. The `apps` dataset contains 492 duplicates rows and 10349 unique rows.
# 4. `Last Updated` column has a object datatype.
# 5. `Rating`,`Current Ver`, `Andriod Ver` `Type` columns contains missing values
# 6. Some columns contains irrelevant values that must be cleaned or removed.

# ### Subtask 1 : Removing Duplicate Rows
# 
# We have established that 492 columns in the apps dataset contains duplicate rows. We would then attempt to remove those duplicate rows from our apps dataset.

# In[7]:


# Drop all duplicate rows that appears more than once in 'Apps' dataset while retaining its first row 
apps.drop_duplicates(keep='first', inplace=True)


# In[8]:


#Check to make sure duplicates rows were dropped
apps.info()


# ### SubTask 2: Remove Irrelevant values from each column if any
# 
# We would check each column to ascertain attributes that are irrelevant and must be removed from the dataset.
# 
# We would start by checking the unique attributes for each column so as to source for irregularities.

# In[9]:


apps['Category'].unique()


# The `category` column loos okay except the 1.9 attribute as seen above which is not a google playstore category and thus we would attempt to remove the row entry containing the category of '1.9'

# In[10]:


#Check the row that contains the category of 1.9
apps[apps['Category'] == '1.9']


# In[11]:


# only one row (row 10472) contain the category of 1.9 and that row should be removed form our dataset since its not needed.

apps.drop('Life Made WI-Fi Touchscreen Photo Frame', inplace=True)


# In[12]:


# Check to make sure the category of 1.9 was removed.

apps['Category'].unique()


# In[13]:


# Check the distinct attributes of `Rating` column
apps['Rating'].unique()


# The Rating column contains missing values. Since the Ratings for each app is a numerical value, these missing values will be replaced with 0.

# In[14]:


#replace all nan values with 0
apps['Rating'] = apps['Rating'].fillna(0)


# In[15]:


# Check the Rating column to confirm that missing nan rows have been filled with 0
apps['Rating'].unique()


# In[16]:


# Check the distinct attributes of `Reviews` column
apps['Reviews'].unique()


# In[17]:


# Check the distinct attributes of `Size` column
apps['Size'].unique()


# In[18]:


# Check the distinct attributes of `Installs` column
apps['Installs'].unique()


# In[19]:


# Check the distinct attributes of `Price` column
apps['Price'].unique()


# In[20]:


# Check the distinct attributes of `Genres` column
apps['Genres'].unique()


# In[21]:


# Check the `Current Ver` column for null values
apps[apps['Current Ver'].isna()]


# In[22]:


# Check the count of null values in `Current Ver` column
apps['Current Ver'].isna().value_counts()


# In[23]:


# Check the count of null values in `Andriod Ver` column
apps['Android Ver'].isna().value_counts()


# In[24]:


# Check the distinct attributes of `Andriod Ver` column
apps['Android Ver'].unique()


# In[25]:


# Drop null values in `Andriod Ver` column
apps.dropna(subset=['Android Ver'], inplace=True)


# In[26]:


# Check the distinct attributes of `Content Rating` column
apps['Content Rating'].unique()


# In[27]:


# Check for unique column attributes
apps['Type'].unique()


# In[28]:


# Drop rows with missing values in `Type` column
apps.dropna(subset=['Type'], inplace=True)


# #### Check
# 
# Let's confirm that the nan row has been removed from the `Type` column

# In[29]:


apps['Type'].unique()


# #### Next is to check for incorrect datatype in column attributes. The `Last Updated` column has a datatype of object and must be changed to a datatype of datetime to reflect the date attributes in it

# In[30]:


# Change datatype of `Last Updated` column to datetime

apps['Last Updated'] = pd.to_datetime(apps['Last Updated'])


# In[31]:


# Let's check that all changes made are reflected in every column.
apps.info()


# ### Summary of Data Cleaning on `Apps` Dataset
# 
# 1. Removed all duplicate rows in the apps dataset.
# 2. Removed 1no. row containing '1.9' in the `Category` variable.
# 3. Replaced all missing values in `Rating` variable with 0.
# 4. Removed all rows containing missing values in `Andriod Ver` variable.
# 5. Removed all rows containing missing values in `Type` variable.
# 6. Changed the datatype of `Last Updated` variable to datetime.

# From the above assessment, it can be seen that the `app` dataset still contains missing values in the `Current Ver` columns which will be addressed in the next stage of our analysis using Microsoft Excel. All missing values in the `Current Ver` column will be replaced with NaN.

# #### Now we can export our `apps` dataset to csv file for further assessment/analysis

# In[32]:


apps.to_csv('cleaned_apps_v2.csv', encoding = 'utf=8')


# ### Data Preparation
# 
# The following data preparation processes was carried out on the cleaned apps dataset after exporting the cleaned apps dataset to csv.
# 
# 1. Replaced all missing values in the `Current Ver` variable with NaN (Carried out on Microsoft Excel)
# 2. Cleaned the apps columns for special characters and irrelevant app names.
# 
#  After data preparation, the cleaned apps dataset was found to contain 9766 rows and 13 variables
#  
#  This cleaned apps dataset can now be analyzed to gain insight using MySQL and visualized using Power BI.

# ## Pre-processing on the `review` dataset

# Lets programmatically view the reviews dataset to get familiar with its properties.

# In[33]:


# Check for dataet dimensions
reviews.shape


# In[34]:


# Lets see the column attributes for reviews dataset
reviews.info()


# In[35]:


# Check dataset to view the first 10 rows
reviews.head(10)


# In[36]:


# Check for missing values in the `Translated_Review` column
reviews['Translated_Review'].isna().value_counts()


# ### Summary of finding on `reviews` dataset
# 
# 1. `reviews` dataset contains 64295 rows and 4 variables
# 2. The dataset contains a lot of missing values for different reviews records
# 3. The `App` column was used as the index column
# 
# #### Sub-task - Drop all rows with missing values

# In[37]:


# Drop all missing values in the reviews dataaset
reviews.dropna(inplace=True)


# We could observed that the `reviews` dataset had 26868 null values in its `Translated_Review` column. Therefore all rows with null values in the `Translated_Review` column was deleted as there is no translated reviews present and as such that kind of data is of no use for our analysis

# #### Check
# 
# Check to make sure all missing values in the reviews dataset was dropped.

# In[38]:


# Check for any remaining missing values in `Transalated_Reviews` column
reviews['Translated_Review'].isna().value_counts()


# In[39]:


# Check for duplicates 
reviews.duplicated().value_counts()


# In[40]:


# Check dataset to confirm that all data cleaning has reflected.
reviews.info()


# _Duplicate records in the reviews dataset would not be dropped as all reviews records will be useful for further analysis_

# ### Summary of Data Cleaning on `reviews` dataset
# 
# 1. All rows containing missing values were dropped from the dataset.
# 2. After dropping missing values the dataset now contains 37427 rows of data

# The reviews dataset will now be exported as a csv file for further analysis

# In[41]:


reviews.to_csv('cleaned_reviews_v2.csv', encoding = 'utf=8')

