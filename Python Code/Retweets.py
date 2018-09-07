import csv
def main():
    t = []
    src_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Base Data/RT_LP.csv", "rt")
    src = csv.reader(src_handle)
    dest_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/RT_LP_ext.csv", "wb")
    dest = csv.writer(dest_handle)
    for row in src:
        t.append(row[1])
        t.append(row[13])
        t.append(row[12])
        t.append(row[11])
        dest.writerow(t)
        del t[:]

    src_handle.close()
    dest_handle.close()


if __name__ == "__main__":
    main()
