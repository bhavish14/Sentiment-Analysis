import csv

def main():
    src_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Intermediate Data/Spam Detection/My Project/Los Angeles {tweet, spam, screenN}.csv", "rb")
    src = csv.reader(src_handle)

    dest_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Intermediate Data/Spam Detection/My Project/Los Angeles {spam}.csv", "wb")
    dest = csv.writer(dest_handle)

    for row in src:
        if row[1] == '1':
            dest.writerow(row)


    src_handle.close()
    dest_handle.close()

if __name__ == "__main__":
    main()
