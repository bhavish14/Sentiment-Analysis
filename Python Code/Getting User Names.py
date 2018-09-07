import re
import csv

def main():
    t = []
    src_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Base Data/Trump_RT_EXT.csv", "rt")
    src = csv.reader(src_handle)
    dest_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Intermediate Data/Exp 2/User_names.csv", "wb")
    dest = csv.writer(dest_handle)
    for row in src:
        match = re.search('([\w\W\s]+)@([\w\W\s]+):([\w\W\s]+)', row[0])
        if match:
            print match.group(2)
            t.append(row[0])
            t.append(match.group(2))
            t.append(row[1])
            t.append(row[2])
            #print(t)
            dest.writerow(t)
        del t [:]
    src_handle.close()
    dest_handle.close()

if __name__=="__main__":
    main()
