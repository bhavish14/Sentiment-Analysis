#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import re
import numpy as np
import random
import multiprocessing

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""




'''

def list_append(count, id, out_list):
	"""
	Creates an empty list and then appends a
	random number to the list 'count' number
	of times. A CPU-heavy operation!
	"""
	for i in range(count):
		out_list.append(random.random())

if __name__ == "__main__":
	size = 10000000000   # Number of random numbers to add
	procs = 5   # Number of processes to create

	# Create a list of jobs and then iterate through
	# the number of processes appending each process to
	# the job list
	jobs = []
	for i in range(0, procs):
		out_list = list()
		process = multiprocessing.Process(target=list_append,
			                              args=(size, i, out_list))
		jobs.append(process)

	# Start the processes (i.e. calculate the random number lists)
	for j in jobs:
		j.start()

	# Ensure all of the processes have finished
	for j in jobs:
		j.join()

	print ("List processing complete.")
'''












def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method

	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#initialize a list to hold all the tweepy Tweets
	alltweets = []

	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	#print (new_tweets[1])

	#save most recent tweets
	alltweets.extend(new_tweets)

	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		#print ("getting tweets before %s") %(oldest)

		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		#save most recent tweets
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		#print ("...%s tweets downloaded so far") % (len(alltweets))

	#transform the tweepy tweets into a 2D array that will populate the csv
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

	#write the csv
	with open('.../dest.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)

	pass

def get_data(user_ids):
	for item in user_ids:
		get_all_tweets(item)



if __name__ == '__main__':	
	username = ''
	#source = csv.reader(source_handle)
	procs = 8   # Number of processes to create

	# Create a list of jobs and then iterate through
	# the number of processes appending each process to
	# the job list
	list_names = []
	for t in range(8):
		temp = []
		temp.append(username[range((t * int(len(username)/8)), ((t + 1) * int(len(username)/8)))])
		list_names.append(temp)

	jobs = []
	for i in range(0, procs):
		out_list = list()
		process = multiprocessing.Process(target=get_data,
			                              args=(list_names[i]))
		jobs.append(process)

	# Start the processes (i.e. calculate the random number lists)
	for j in jobs:
		j.start()

	# Ensure all of the processes have finished
	for j in jobs:
		j.join()

	print ("List processing complete.")

