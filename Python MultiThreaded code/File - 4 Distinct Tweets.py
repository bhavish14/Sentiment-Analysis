import csv
import numpy as np
import random
import multiprocessing
import os
import pandas as pd
def remove_duplicates(file_source):
    src_handle = open('' % file_source, "r")
    src = csv.reader(src_handle)
    tweets = list(src)
    Tweets = np.array(tweets)
    Tweets = Tweets[:,2]
    tweets_set = set(Tweets)
    tweet_df = pd.DataFrame(list(tweets_set))
    tweet_df.to_csv('' % file_source, index=False, header=True)


def data_handle(list):
	for item in list:
		remove_duplicates(item)

#id, created, text = np.loadtxt('', delimiter=',', unpack = True, dtype='str')
#src_handle = open('', "rb")
def main():
    file_names = os.listdir('')
    procs = 8
    list_names = []
    length = int(len(file_names)/8)
    for t in range(8):
        temp = []
        temp.append(file_names[(t * length):((t + 1) * length)])
        list_names.append(temp)

    jobs = []
    for i in range(0, procs):
        out_list = list()
        process = multiprocessing.Process(target=data_handle, args=(list_names[i]))
        jobs.append(process)

    # Start the processes (i.e. calculate the random number lists)
    for j in jobs:
        j.start()

    # Ensure all of the processes have finished
    for j in jobs:
        j.join()

    print ("List processing complete.")

if __name__ == '__main__':
    main()
