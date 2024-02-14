
'''Part one Load data and explore'''
import pandas as pd

# Load the data to a single DataFrame.
path = r'C:\Users\TruongJ\Documents\Github\python\04-assignments\ttc-bus-delay-data-2023 (1).xlsx'
bus_data = pd.read_excel(path)


# In[9]:


'''2. Profile the DataFrame.
   * What are the column names?
   * What are the dtypes when loaded? Do any not make sense? Yes there are a ot of object data types. Eg Day should be int
   * How many NaNs are in each column?
   * What is the shape of the DataFrame"Assignment 2.doc'''

bus_data.info()


  
   


# In[12]:


#Count total number of NAN in each column
bus_data.isna().sum()


# In[15]:


bus_data.shape


# In[167]:


'''3. Generate some summary statistics for the data.
   * For numeric columns: What are the max, min, mean, and median?
   * For text columns: What is the most common value? How many unique values are there?
   * Are there any statistics that seem unexpected? There are a lot of NaN's
4. Rename one or more columns in the DataFrame.
5. Select a single column and find its unique values.
6. Select a single text/categorical column and find the counts of its values.
7. Convert the data type of at least one of the columns. If all columns are typed correctly, convert one to `str` and back.
8. Write the DataFrame to a different file format than the original.'''"Assignment 2.docx"

bus_data.describe(include='all')


# In[ ]:


'''4. Rename one or more columns in the DataFrame.'''


bus = bus_data.rename(columns={'Day':'Day_Of_Week'})
bus





# In[23]:


'''
5. Select a single column and find its unique values.'''

bus_data['Location'].unique()


# In[37]:


''''6. Select a single text/categorical column and find the counts of its values.'''

bus_data['Day'].value_counts
#7
bus_data['Location'].astype(str)





# In[45]:


#8. Write the DataFrame to a different file format than the original.

import os
cwd = os.getcwd()

bus_data.to_csv


# In[54]:


### More data wrangling, filtering
'''1. Create a column derived from an existing one. Some possibilities:
   * Bin a continuous variable
   * Extract a date or time part (e.g. hour, month, day of week)
   * Assign a value based on the value in another column (e.g. TTC line number based on line values in the subway delay data)
   * Replace text in a column (e.g. replacing occurrences of "Street" with "St.")'''

bus_data['Hour Delay'] = bus_data['Min Delay'].astype(int)//60

#bus_data


# In[56]:


'''2. Remove one or more columns from the dataset.'''

bus_data = bus_data.drop(['Hour Delay'], axis=1)
bus_data.head()


# In[81]:


'''3. Extract a subset of columns and rows to a new DataFrame
   * with the `.query()` method and column selecting `[[colnames]]`
   * with `.loc[]`'''
   

bus_data.loc[bus_data['Day'] == ('Monday')]
   
bus_data.query('`Min Delay` < 20') 


# In[88]:


'''4. Investigate null values
   * Create and describe a DataFrame containing records with NaNs in any column
   * Create and describe a DataFrame containing records with NaNs in a subset of columns
   * If it makes sense to drop records with NaNs in certain columns from the original DataFrame, do so.'''


No_directions = bus_data.loc[bus_data['Direction'].isna()]
bus_data.loc[bus_data['Incident'] == 'Security',
            ['Incident', 'Direction', 'Date', 'Time']]


# In[166]:


bus_data.dropna


# In[154]:


'''### Grouping and aggregating
1. Use `groupby()` to split your data into groups based on one of the columns.
2. Use `agg()` to apply multiple functions on different columns and create a summary table. Calculating group sums or standardizing data are two examples of possible functions that you can use.
'''


bus_data.groupby(['Day']).mean()



Daily_bus_data = bus_data.groupby(['Day'])


Summary_table = Daily_bus_data.agg(Delay_counts = ('Min Delay', 'count'),Mean_Delay=('Min Delay','mean'),
                   Mean_Gap= ('Min Gap', 'mean'))


# In[119]:


Summary_table


# In[165]:


'''1. Plot two or more columns in your data using `matplotlib`, `seaborn`, or `plotly`. Make sure that your plot has labels, a title, a grid, and a legend.'''


import matplotlib.pyplot as plt

Summary_table.plot(y=["Mean_Delay", "Mean_Gap"], kind='bar', ylabel= 'Mean Delays (min)').grid()

