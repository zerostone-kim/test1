# https://github.com/zerostone-kim/test1/blob/master/MovieLense.ipynb
# 위 link 로 들어가서 "open in colab" 클릭하시면 작업 수행 확인 가능합니다.

import pandas as pd

movies = pd.read_csv('test1/ml-latest-small/movies.csv')
tags = pd.read_csv('test1/ml-latest-small/tags.csv')
ratings = pd.read_csv('test1/ml-latest-small/ratings.csv')

print(ratings.columns)
# print(ratings.describe())
# max_rating_userId = ratings[ratings['rating'] == max_rating]

# 사용자별 MIN / MAX 평점
max_rating = userId_mean['rating'].max()
min_rating = userId_mean['rating'].min()

max_rating_userId = userId_mean[userId_mean.rating == max_rating]
min_rating_userId = userId_mean[userId_mean.rating == min_rating]

print('1. 최고평점 userId : ' + ','.join(map(str, max_rating_userId.index.tolist())))
print('2. 최저평점 userId : ' + ','.join(map(str, min_rating_userId.index.tolist())))

merge_movies_ratings = pd.merge(movies, ratings, how='inner', on='movieId')
max_ratings_movies_gb = merge_movies_ratings.groupby('movieId').max()
min_ratings_movies_gb = merge_movies_ratings.groupby('movieId').min()

max_rating = max_ratings_movies_gb.rating.max()
min_rating = min_ratings_movies_gb.rating.min()

max_movie_rating = max_ratings_movies_gb[max_ratings_movies_gb.rating == max_rating]
min_movie_rating = min_ratings_movies_gb[max_ratings_movies_gb.rating == min_rating]

print('3. 최고평점 : '+','.join(max_movie_rating.title))
print('4. 최저평점 : '+','.join(min_movie_rating.title))
