import csv
import numpy as np


def main():
    username, positive, negative, neutral, no_tweets = np.genfromtxt('', delimiter=',', skip_header = 1, unpack = True, dtype='str')
    list_t = []
    des_handle = open('', "w")
    des = csv.writer(des_handle)
    des.writerow(['Username', 'Positive Tweets', 'Negative Tweets', 'Neutral Tweets'])
    for i in range(len(username)):
        list_t.append(username[i])
        p = float(positive[i])
        n = float(negative[i])
        nn = float(neutral[i])
        nos = float(no_tweets[i])
        pos_ratio = p/nos
        neg_ratio = n/nos
        neutral_ratio = nn/nos
        list_t.append(pos_ratio)
        list_t.append(neg_ratio)
        list_t.append(neutral_ratio)
        des.writerow(list_t)
        del list_t[:]


if __name__ == '__main__':
    main()
