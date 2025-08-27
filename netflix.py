import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# step1 -> load the netflix dataset using pandas 
df = pd.read_csv(r"C:\Users\HP\Downloads\netflix_titles.csv.zip")

# step2 -> data clean and find missing values 
print(df.isnull().sum())
df = df.dropna(subset=['release_year','type','country','rating','duration']) # drop all the null values

# task1 -> create a bar chart to compare movies and tv shows 
type_counts = df['type'].value_counts()
print(type_counts.index)
print(type_counts.values)
plt.figure(figsize=(6,4))
plt.bar(type_counts.index,type_counts.values,color=['skyblue','orange'])
# type_counts.index -> unique category names ie. ['Movies','tvshows'] x-axis pr show krna
# type_counts.values -> har type ka count [5687,2283] y-axis pr show krna
plt.title("No. of movies VS tv shows on netflix")
plt.xlabel("Type")
plt.ylabel("count")
plt.tight_layout()
plt.savefig("movies_vs_tvshows.png")
plt.show()

#task2 -> percentage of each content rating
rating_counts = df['rating'].value_counts()
print(rating_counts)
plt.figure(figsize=(8,6))
plt.pie(rating_counts,labels=rating_counts.index,autopct='%1.1f%%', startangle=90)
plt.title("Percentage of content rating on netflix")
plt.tight_layout()
plt.savefig("content_ratings.png")
plt.show()

#task3 -> distribution of movies durations
movies = df[df['type'] == 'Movie'] # sirf movies type ko select krega (not tvshow type)
movies['duration'] = movies['duration'].dropna().str.replace('min','').astype(int)
# ye nan values of duration ko hatayega (iski koi khas jarurat nahi because already upar dropna()kiya hai)
# and replace string (minutes)
plt.figure(figsize=(6,4))
plt.hist(movies['duration'],bins=20,color='purple',edgecolor='black')
plt.title("movie duration on netflix")
plt.xlabel("duration (mins)")
plt.ylabel("Number of movies")
plt.tight_layout()
plt.savefig("movie_duration.png")
plt.show()

# task4 -> realtionship between release_year and no. of shows
release_counts = df['release_year'].value_counts().sort_index()
print(release_counts)
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index, release_counts.values, color='red')
plt.title("Release years VS no. of tvshows on netflix")
plt.xlabel("Release year")
plt.ylabel("Number of shows")
plt.tight_layout()
plt.savefig("release_year.png")
plt.show()

# task5 -> top 10 countries with the highest no. of shows 
country_counts = df['country'].value_counts().head(10) # we only want 10 countries 
plt.figure(figsize=(8,6))
plt.barh(country_counts.index , country_counts.values, color='red')
plt.title("Top 10 countries with the highest no. of shows on netflix")
plt.xlabel("No. of shows")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("top10_shows.png")
plt.show()

# task6 -> compare multiple plots together, here compare movies and tvshows with year 
content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)
"""groupby >year and type(movie or tvshow), size()- counts the no. of columns in each row , unstack- turn the type
(movie and tvshow) into column making it dataframe, fillna(0) -> fill the null values with 0
"""
fig, ax = plt.subplots(1,2, figsize=(12,5))
# first subplot: movies 
ax[0].plot(content_by_year.index, content_by_year['Movie'],color='blue')
ax[0].set_title('movies released per year')
ax[0].set_xlabel('year')
ax[0].set_ylabel('Number of movies')

# second subplot: tvshows
ax[1].plot(content_by_year.index, content_by_year['TV Show'],color='orange')
ax[1].set_title('shows released per year')
ax[1].set_xlabel('year')
ax[1].set_ylabel('Number of shows')

fig.suptitle('comparison of movies and tv shows release over years on netflix')
plt.legend()
plt.tight_layout()
plt.savefig("comparison.png")
plt.show()
