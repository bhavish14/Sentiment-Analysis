import csv

def main():
    src_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Intermediate Data/Project1 {Word List}.csv", 'r', encoding = "ISO-8859-1")
    src = csv.reader(src_handle)
    dest_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Intermediate Data/Project1 {Word List Refined}.csv", 'w')
    dest = csv.writer(dest_handle)
    word_list = []
    for row in src:
        for item in src:
            word_list.append(item)
        dest.writerow(word_list)
        del word_list [:]

if __name__ == "__main__":
    main()
