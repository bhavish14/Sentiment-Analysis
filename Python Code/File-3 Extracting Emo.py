import csv
def main():
        src_handle = open("/mnt/windows/Projects/Sentiment Analysis/Project - Product Review/CSV Files/Intermediate Data/Samsung Tokenized(17-07-17).csv", "r", encoding = "ISO-8859-1")
        src = csv.reader(src_handle)
        dest_handle = open("/mnt/windows/Projects/Sentiment Analysis/Project - Product Review/CSV Files/Intermediate Data/Samsung Emoji(17-07-17).csv", "w")
        dest = csv.writer(dest_handle)
        t = []
        Emo = ["(:", ":3", ":-'(", ":/", ":-/", "):", "-(", ")"":-)",":)",":]","=)",";-)",";)",":-D",":D","=D",":\\", ":-*",":*","O:)","O:-)", ":-P",":P",":-p",":p","=P", ":-(", ":(", ":[", "=(", "=(:", ":-O", ":O", ":-o", ":o", ":'(", ":-|"]

        i = 1

        for row in src:
            for item in row:
                for e in Emo:
                    if e in item:
                        #print (item)
                        t.append(e)
                    #print (i, " ", t)
            dest.writerow(t)
            #i = i + 1
            del t[:]
        '''
        i = 1
        for row in src:
            if i == 25:
                print (row)
                for item in row:
                    for e in Emo:
                        if e in item:
                            print (item)
                            t.append(e)
                            print (i, " ", t)
            del t [:]
            i = i + 1
        '''

if __name__ == "__main__":
    main()
