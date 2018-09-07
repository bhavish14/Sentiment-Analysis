import csv

def main():
    happy = [":-)",":)",":]","=)",";-)",";)",":-D",":D","=D",":-*",":*","O:)","O:-)"]
    funny = [":-P",":P",":-p",":p","=P",":3"]
    sad = [":-(",":(",":[","=(",":-O",":O",":-o",":o",":'("]

    src_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Base Data/Project 1 Base File.csv", "r", encoding = "ISO-8859-1")
    src = csv.reader(src_handle)
    dest_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Base Data/Project 1 Emoji {pos-neg}.csv", "w")
    dest = csv.writer(dest_handle)

    pos = 0
    neg = 0
    funn = 0

    for row in src:
        for h in happy:
            if h in row[3]:
                pos = pos + 1
        for n in sad:
            if n in row[3]:
                neg = neg + 1
        for fun in funny:
            if fun in row[3]:
                funn = funn + 1
        if pos > 0 and neg > 0:
            dest.writerow([row[3]])
        pos = 0
        neg = 0
        funn = 0

    src_handle.close()
    dest_handle.close()

if __name__ == "__main__":
    main()
