#!/usr/bin/env python3

# -------
# imports
# -------

from math import sqrt
import pickle
from requests import get
from os import path
from numpy import sqrt, square, mean, subtract


def create_cache(filename):
    """
    filename is the name of the cache file to load
    returns a dictionary after loading the file or pulling the file from the public_html page
    """
    cache = {}
    filePath = "/u/fares/public_html/netflix-caches/" + filename

    if path.isfile(filePath):
        with open(filePath, "rb") as f:
            cache = pickle.load(f)
    else:
        webAddress = "http://www.cs.utexas.edu/users/fares/netflix-caches/" + \
            filename
        bytes = get(webAddress).content
        cache = pickle.loads(bytes)

    return cache


AVERAGE_RATING = 3.60428996442

#This is a dictionary of (customer_id, movie_id) as keys (int, int) and their actual rating as values (int
ACTUAL_CUSTOMER_RATING = create_cache(
    "cache-actualCustomerRating.pickle")

#This is a cache of (movieId, year) as keys (int, int) and it's average rating for that year as values (float)
AVERAGE_MOVIE_RATING_PER_YEAR = create_cache(
    "cache-movieAverageByYear.pickle")

#This is a cache of (customerId, movieId ) as keys (int, int) and the year the movie was rated by that customer as a value (int
YEAR_OF_RATING = create_cache("cache-yearCustomerRatedMovie.pickle")

#This is a cache of (customerId, year) as keys (int, int) and then a float of their average rating for the year as the value (float)
CUSTOMER_AVERAGE_RATING_YEARLY = create_cache(
    "cache-customerAverageRatingByYear.pickle")


'''
#actual_scores_cache = {10040: {2417853: 1, 1207062: 2, 2487973: 3}}
actual_scores_cache = {}
cust_id_rating = {}
for item in ACTUAL_CUSTOMER_RATING.items():
    customer_id = item[0][0]
    movie_id = item[0][1]
    rating = item[1]
    cust_id_rating[customer_id] = rating 
    actual_scores_cache[movie_id] = cust_id_rating
print(actual_scores_cache)

#movie_year_cache = {10040: 1990}
movie_year_cache = {}
for item in AVERAGE_MOVIE_RATING_PER_YEAR.items():
    movie_id = item[0][0]
    year = item[0][1]
    rating = item[1]
    movie_year_cache[movie_id] = year
print(movie_year_cache)

decade_avg_cache = {1990: 2.5, 2000: 2.6}
decade_avg_cache = {}
decade_ratings = {199: [], 200: []}
for movie in actual_scores_cache:
    for film in movie_year_cache:
        if movie == film:
            year = (movie_year_cache[film] // 10)
            if year in decade_ratings:
                a_films_ratings = []
                for user_id in actual_scores_cache[movie]:
                    a_films_ratings.append(actual_scores_cache[movie][user_id])
                decade_ratings[year].append(a_films_ratings)

print(decade_ratings)
'''




# ------------
# netflix_eval
# ------------

def netflix_eval(reader, writer) :
    predictions = []
    actual = []

    AVERAGE_RATING = 3.60428996442

    # iterate throught the file reader line by line
    for line in reader:
    # need to get rid of the '\n' by the end of the line
        line = line.strip()
        # check if the line ends with a ":", i.e., it's a movie title 
        if line[-1] == ':':
            movie = int(line.rstrip(':'))
		# It's a movie
            # current_movie = line.rstrip(':')
            # pred = movie_year_cache[int(current_movie)]
            # pred = (pred // 10) *10
            # prediction = decade_avg_cache[pred]
            # writer.write(line)
            # writer.write('\n')
            # current_movie = line.rstrip(':')
        else:
		# It's a customer
            # current_customer = line
            # predictions.append(prediction)
            # actual.append(actual_scores_cache[int(current_movie)][int(current_customer)])
            # writer.write(str(prediction)) 
            # writer.write('\n')
            current_customer = line
            actual.append(ACTUAL_CUSTOMER_RATING[(int(current_customer), movie)])
            predictions.append(AVERAGE_RATING)	
    # calculate rmse for predications and actuals
    rmse = sqrt(mean(square(subtract(predictions, actual))))
    writer.write(str(rmse)[:4] + '\n')

