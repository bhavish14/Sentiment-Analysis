import csv

def main():
    tweet = []
    retweet_id = []
    tweet_count = []
    t = []
    src_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Base Data/Trump_RT_EXT.csv", "rt")
    src = csv.reader(src_handle)
    dest_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Intermediate Data/Trump_RT.csv", "wb")
    dest = csv.writer(dest_handle)
    for row in src:
        tweet.append(row[0])
        retweet_id.append(row[1])
        tweet_count.append(row[2])
    #print(tweet, retweet_id, tweet_count)
    max_t = max(tweet_count)
    threshold = int(max_t) / 8
    st = 0
    for item in range(len(tweet)):
        if int(tweet_count[item]) > threshold:
            st = 1
        else:
            st = 0
        t.append(tweet[item])
        t.append(retweet_id[item])
        t.append(tweet_count[item])
        t.append(st)
        dest.writerow(t)
        del t[:]

    print(max_t)
    src_handle.close()
    dest_handle.close()

if __name__ == "__main__":
    main()
