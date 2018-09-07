import csv

def main():
    src_handle = open("/mnt/windows/Projects/Sentiment Analysis/usage of # to trend/CSV Files/Base Data/#SamjhautaSecretTape.csv", 'rb')
    src = csv.reader(src_handle)

    dest_handle = open("/mnt/windows/Projects/Sentiment Analysis/usage of # to trend/CSV Files/Base Data/#SamjhautaSecretTape(25-7).csv",'wt')
    dest = csv.writer(dest_handle)
    t = []
    for row in src:
        t.append(row[1])
        #t.append(row[5])
        #t.append(row[10])
        #t.append(row[11])
        #t.append(row[12])
        #t.append(row[15])
        #t.append(row[16])
        dest.writerow(t)
        del t[:]

    src_handle.close()
    #src_handle1.close()
    #src_handle2.close()
    #src_handle3.close()
if __name__ == "__main__":
    main()
