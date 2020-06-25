import pandas as pd
import seaborn as sns
#lets import numpy just for in case
import numpy as np
column_names= ['user_id','movie_name', 'rating']
path = 'C:/Users/lenovo/Desktop/movies.csv'
data = pd.read_csv(path,sep='\t', names=column_names) 
data.head()
data.groupby('movie_rating')['rating'].mean().sort_values(ascending=False).head()
ratings = pd.DataFrame(data.groupby('movie_rating')['rating'].mean())
ratings['num of rating'] = pd.DataFrame(data.groupby('movie_rating')['rating'].count())
ratings.head()
ratings.tail()
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
%matplotlib inline
plt.figure(figsize=(10,4))
ratings['num of rating'].hist(bins = 70)
ratings.tail()
plt.figure(figsize = (20,4))
ratings['rating'].hist(bins=70)
moviesmat = data.pivot_table(index='id', columns = 'movie_rating', values='rating')
moviesmat.head()
ratings.sort_values('num of rating',ascending =False).head(20)
parasite_user_rating = moviesmat['Parasite']
greenzone_user_rating = moviesmat['Green Zone']
parasite_user_rating.head()
similar_to_parasite = moviesmat.corrwith(parasite_user_rating)
similar_to_greenzone = moviesmat.corrwith(greenzone_user_rating)
corr_parasite = pd.DataFrame(similar_to_parasite,columns=['Correlation'])
corr_greenzone = pd.DataFrame(similar_to_greenzone,columns=['Correlation'])
corr_parasite.head()
corr_parasite.sort_values('Correlation', ascending= False).head()
corr_parasite= corr_parasite.join(ratings['num of rating'])
corr_parasite.head()
corr_parasite[corr_parasite['num of rating']>100].sort_values('Correlation',ascending = False).head()
corr_greenzone = pd.DataFrame(similar_to_greenzone, columns =['Correlation']) 
corr_greenzone.dropna(inplace = True) 
corr_greenzone = corr_greenzone.join(ratings['num of rating']) 
corr_greenzone[corr_greenzone['num of rating']>100].sort_values('Correlation', ascending = False).head()
