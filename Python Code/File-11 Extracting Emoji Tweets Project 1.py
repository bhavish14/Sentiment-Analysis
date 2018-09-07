import csv

def main():
    t = []
    src_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Base Data/Project 1 Base File.csv", "r", encoding = "ISO-8859-1")
    src = csv.reader(src_handle)
    dest_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Base Data/Project 1 Emoji.csv", "w")
    dest = csv.writer(dest_handle)
    Emo = [":-)",":)",":]","=)",";-)",";)",":-D",":D","=D",":-*",":*","O:)","O:-)", ":-P",":P",":-p",":p","=P",":3", ":-(",":(",":[","=(",":-O",":O",":-o",":o",":'("]

    for row in src:
        for item in Emo:
            if item in row[3]:
                dest.writerow([row[3]])
    src_handle.close()
    dest_handle.close()

if __name__ == "__main__":
    main()
