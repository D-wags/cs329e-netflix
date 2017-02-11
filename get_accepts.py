from math import sqrt
import pickle
from requests import get
from os import path
from numpy import sqrt, square, mean, subtract
import sys


#10040:
#2417853
#1207062
#2487973


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

# {(custid movieid): year}
test_cache = create_cache("cache-yearCustomerRatedMovie.pickle")

# {movie: userid}
new_dict = {}
for item in test_cache:
	#print(item)
	if item[1] not in new_dict:
		new_dict[item[1]] = [item[0]]
	else:
		new_dict[item[1]].append(item[0])

#netflix_eval(sys.stdin, sys.stdout)

# writer = sys.stdin

writer = open("RunNetflix.in", 'w')
for item in new_dict:
	writer.write(str(item) + ":")
	writer.write('\n')

	writer.write(str(new_dict[item][0]))
	writer.write('\n')

	if len(new_dict[item]) > 1:
		writer.write(str(new_dict[item][1]))
		writer.write('\n')

	if len(new_dict[item]) > 2:
		writer.write(str(new_dict[item][2]))
		writer.write('\n')

	if len(new_dict[item]) > 3:
		writer.write(str(new_dict[item][3]))
		writer.write('\n')
	

writer.close()
	

