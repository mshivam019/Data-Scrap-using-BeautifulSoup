#!/usr/bin/env python
# coding: utf-8

# # IMDB - Web Scraping with Beautiful Soup

# ### Step 1: Import Libraries

# In[286]:


from bs4 import BeautifulSoup # For parsing the HTML page
import pandas as pd # Data Manipulation and export
from requests import get # Request URL to access content


# ### Step 2: Create a variable url which contains the link

# In[287]:


url = 'http://www.imdb.com/search/title?release_date=2021&sort=num_votes,desc&page=1'
response = get(url)


#  ### Step 3: Print the response

# In[288]:


print(response.text)


#  ### Step 3: Use Beautiful Soup to parse the data

# In[289]:


html_soup = BeautifulSoup(response.text, 'html')


# In[290]:


movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
first_movie = movie_containers[0]
i=0


# ### Step 4: Initiliaze the lists

# In[291]:


names = []
years = []
imdb_ratings = []
votes = []


# ### Step 5: Start storing the data

# In[292]:


for countainer in movie_containers:
    name = countainer.h3.a.text
    names.append(name)
    year = countainer.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
    start_year = year.find('2')
    years.append(year[start_year:start_year+4])
    imdb_rating = float(countainer.strong.text)
    imdb_ratings.append(imdb_rating)
    vote = int(countainer.find('span', attrs = {'name':'nv'})['data-value'])
    votes.append(vote) 


# ### Step 6: Verify the stored data

# In[293]:


print(names)
print(years)
print(imdb_ratings)
print(votes)    


# ### Step 7: Store the data

# In[294]:


df = pd.DataFrame({'Name':names, 'Year':years, 'Rating':imdb_ratings, 'Vote':votes})
df.to_excel('movies.xlsx', index=False, encoding='utf-8')


# ### Step 8: Check the final output

# In[295]:


df.head()


# In[ ]:




