import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing the CSV file
dataset = pd.read_csv('books.csv')
dataset = dataset[(dataset.language_code =='eng')|(dataset.language_code =='eng-US')|(dataset.language_code =='eng-GB')]
print("Dataset contains {} rows and {} columns".format(dataset.shape[0], dataset.shape[1]))
print(dataset.isnull().sum())

print("Earliest publication: {}".format(dataset.publication_date.min()))
print("Most recent publication: {}".format(dataset.publication_date.max()))
#finding most rated books
most_rated_books = dataset.sort_values('ratings_count', ascending = False).head(50).set_index('title')
print(most_rated_books)
plt.plot(most_rated_books['ratings_count'], most_rated_books.index, color = 'red')
plt.xlabel('Ratings out of 5')
plt.ylabel('Name of book')
plt.show()            
#finding books with high average rating
high_average_rating =dataset[dataset['ratings_count'] > 2000000]
high_average_rating = high_average_rating.sort_values('average_rating',ascending=False).head(25).set_index('title')
print(high_average_rating)
plt.bar(high_average_rating['average_rating'], high_average_rating.index, color = 'black')
plt.xlabel('Ratings out of 5')
plt.ylabel('Name of book')
plt.show()
#books written by author JK Rowling
rowling = dataset[(dataset.authors == 'J.K. Rowling')]
print(rowling.head(15))
#top 10 books based on ratings
top_10_books = dataset[dataset['ratings_count']>1000000].sort_values(by = 'ratings_count', ascending = False).head(10).set_index('title')
print(top_10_books)
#top 10 authors with and their most popular books
book_Aut = dataset.groupby('authors')['title'].count().reset_index().sort_values('title',ascending =False).head(10)
print(book_Aut)
#tp 10 highest rated books
top10_rating = dataset.sort_values('average_rating', ascending=False)[:10]
print(top10_rating)
#top 10 most popular books
top10_pop = dataset.sort_values('text_reviews_count', ascending=False)[:10]
print(top10_pop)




