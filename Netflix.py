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

# {userId:offset value,....}
USER_OFFSET = create_cache(
    "amm7366-rs45899-customerAverageOffset.pickle")

# {movieid:average movie rating,...}
AVERAGE_MOVIE_RATING = create_cache(
    "cache-averageMovieRating.pickle")

#This is a dictionary of (customer_id, movie_id) as keys (int, int) and their actual rating as values (int
ACTUAL_CUSTOMER_RATING = create_cache(
    "cache-actualCustomerRating.pickle")

#actual_scores_cache = {10040: {2417853: 1, 1207062: 2, 2487973: 3}}
actual_scores_cache = {}
cust_id_rating = {}
for item in ACTUAL_CUSTOMER_RATING.items():
    customer_id = item[0][0]
    movie_id = item[0][1]
    rating = item[1]
    cust_id_rating[customer_id] = rating 
    actual_scores_cache[movie_id] = cust_id_rating


# ------------
# netflix_eval
# ------------

def netflix_eval(reader, writer) :
    """ 
    compares user ratings to predictions and returns root mean squared error
    writes predictions and overall error to file 
    """
    predictions = []
    actual = []

    # iterate throught the file reader line by line
    for line in reader:
    # need to get rid of the '\n' by the end of the line
        line = line.strip()
        # check if the line ends with a ":", i.e., it's a movie title 
        if line[-1] == ':':
        # It's a movie
            current_movie = line.rstrip(':')
            pred = AVERAGE_MOVIE_RATING[int(current_movie)]
            assert isinstance(pred, float)
            writer.write(line)
            writer.write('\n')
            

        else:
        # It's a customer
            current_customer = line
            offset = USER_OFFSET[int(current_customer)]
            prediction = pred + offset
            prediction = round(prediction, 1)
            predictions.append(prediction)
            actual.append(actual_scores_cache[int(current_movie)][int(current_customer)])
            writer.write(str(prediction)) 
            writer.write('\n')

    # calculate rmse for predications and actuals
    rmse = sqrt(mean(square(subtract(predictions, actual))))
    writer.write(str(rmse)[:4] + '\n')
    assert isinstance(rmse, float)