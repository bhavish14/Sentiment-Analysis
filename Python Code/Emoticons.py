import csv
happy = [":-)",":)",":]","=)",";-)",";)",":-D",":D","=D",":-*",":*","O:)","O:-)"]
funny = [":-P",":P",":-p",":p","=P",":3"]
sad = [":-(",":(",":[","=(",":-O",":O",":-o",":o",":'("]

file_tweet = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Tokenized data/Tokenized_Apple.csv","rb")
f = csv.reader(file_tweet)

gen_file = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Emo/Apple_emo.csv","wb")
g = csv.writer(gen_file)

found_emo = []

for row in f:
    for item in row:
        for t in happy:
            if item == t:
                found_emo.append(item)
        for t in funny:
            if item == t:
                found_emo.append(item)
        for t in sad:
            if item == t:
                found_emo.append(item)
    g.writerow(found_emo)
    del found_emo[:]
