
# coding: utf-8

# In[14]:

import xlrd
import pprint


# In[15]:

book=xlrd.open_workbook("C:/Users/PRIYANSHU/Downloads/gtd_12to15_0616dist.xlsx")


# In[16]:

sheet=book.sheet_by_name("Data")


# In[17]:

data={}


# In[44]:

len=int(sheet.nrows/500)
for i in range(1,len):
    row=sheet.row_values(i)
    eventid=row[0]
    data[eventid]={
        'iyear':row[1],
        'country_txt':row[8],
        'summary':row[29],
        'targtype1_txt':row[35]
    }


# In[45]:

pprint.pprint(data)


# In[ ]:




# In[ ]:



