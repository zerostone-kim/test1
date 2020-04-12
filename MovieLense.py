# https://github.com/zerostone-kim/test1/blob/master/MovieLense.ipynb
# 위 link 로 들어가서 "open in colab" 클릭하시면 작업 수행 확인 가능합니다.

import pandas as pd

movies = pd.read_csv('test1/ml-latest-small/movies.csv')
tags = pd.read_csv('test1/ml-latest-small/tags.csv')
ratings = pd.read_csv('test1/ml-latest-small/ratings.csv')

print(ratings.columns)
# print(ratings.describe())
# max_rating_userId = ratings[ratings['rating'] == max_rating]

# 사용자별 평균 평점
userId_mean = ratings.groupby('userId').mean()
# 사용자별 MIN / MAX 평점
max_rating = userId_mean['rating'].max()
min_rating = userId_mean['rating'].min()
# MIN/MAX 평점의 사용자들 
max_rating_userId = userId_mean[userId_mean.rating == max_rating]
min_rating_userId = userId_mean[userId_mean.rating == min_rating]

print('1. 최고평점 userId : ' + ','.join(map(str, max_rating_userId.index.tolist())))
print('2. 최저평점 userId : ' + ','.join(map(str, min_rating_userId.index.tolist())))

# movie, ratings 두개의 dataframe 을 조인하여 1개의 dataframe 로 만듦
merge_movies_ratings = pd.merge(movies, ratings, how='inner', on='movieId')

# movieId 기준의 group by 해서 rating 컬럼의 평균을 구함
movies_rating_mean = merge_movies_ratings.groupby('movieId').mean()
max_rating = movies_rating_mean['rating'].max()  
min_rating = movies_rating_mean['rating'].min()

# 최고/최저 평점의 영화 Dataframe 생성
max_movie_df = movies_rating_mean[movies_rating_mean['rating'] == max_rating]
min_movie_df = movies_rating_mean[movies_rating_mean['rating'] == min_rating]

# Title 를 가져오기 위한 Merge
max_movie_list = pd.merge(max_movie_df, movies, left_index = True, right_on = 'movieId', how='left', copy=True)
min_movie_list = pd.merge(min_movie_df, movies, left_index = True, right_on = 'movieId', how='left', copy=True)

print('3. 최고평점 : '+','.join(max_movie_list.title))
print('4. 최저평점 : '+','.join(min_movie_list.title))
