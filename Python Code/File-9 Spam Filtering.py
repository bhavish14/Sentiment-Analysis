import csv

def main():
    src_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Intermediate Data/Spam Detection/My Project/Los Angeles (12-04).csv", "rb")
    src = csv.reader(src_handle)

    commerce_handle = open("/mnt/windows/Repository/Sentiment Analysis/Spam Triggers/Commerce.csv", "rb")
    callAction_handle = open("/mnt/windows/Repository/Sentiment Analysis/Spam Triggers/Calls to Action.csv", "rb")
    description_handle = open("/mnt/windows/Repository/Sentiment Analysis/Spam Triggers/Descriptions.csv", "rb")
    employment_handle = open("/mnt/windows/Repository/Sentiment Analysis/Spam Triggers/Employment.csv", "rb")
    financialBusiness_handle = open("/mnt/windows/Repository/Sentiment Analysis/Spam Triggers/Financial - Business.csv", "rb")
    financialGeneral_handle = open("/mnt/windows/Repository/Sentiment Analysis/Spam Triggers/Financial - General.csv", "rb")
    financialPersonal_handle = open("/mnt/windows/Repository/Sentiment Analysis/Spam Triggers/Financial - Personal.csv", "rb")
    free_handle = open("/mnt/windows/Repository/Sentiment Analysis/Spam Triggers/Free.csv", "rb")
    general_handle = open("/mnt/windows/Repository/Sentiment Analysis/Spam Triggers/General.csv", "rb")
    marketing_handle = open("/mnt/windows/Repository/Sentiment Analysis/Spam Triggers/Marketing.csv", "rb")
    medical_handle = open("/mnt/windows/Repository/Sentiment Analysis/Spam Triggers/Medical.csv", "rb")
    nouns_handle = open("/mnt/windows/Repository/Sentiment Analysis/Spam Triggers/Nouns.csv", "rb")
    numbers_handle = open("/mnt/windows/Repository/Sentiment Analysis/Spam Triggers/Numbers.csv", "rb")
    offers_handle = open("/mnt/windows/Repository/Sentiment Analysis/Spam Triggers/Offers.csv", "rb")
    personal_handle = open("/mnt/windows/Repository/Sentiment Analysis/Spam Triggers/Personal.csv", "rb")
    senseOfUrgency_handle = open("/mnt/windows/Repository/Sentiment Analysis/Spam Triggers/Sense of Urgency.csv", "rb")

    t = [src] * 16

    t[0]= csv.reader(commerce_handle)
    t[1] = csv.reader(callAction_handle)
    t[2] = csv.reader(description_handle)
    t[3] = csv.reader(employment_handle)
    t[4] = csv.reader(financialBusiness_handle)
    t[5] = csv.reader(financialPersonal_handle)
    t[6] = csv.reader(financialGeneral_handle)
    t[7] = csv.reader(free_handle)
    t[8] = csv.reader(general_handle)
    t[9] = csv.reader(marketing_handle)
    t[10] = csv.reader(medical_handle)
    t[11] = csv.reader(nouns_handle)
    t[12] = csv.reader(numbers_handle)
    t[13] = csv.reader(offers_handle)
    t[14] = csv.reader(personal_handle)
    t[15] = csv.reader(senseOfUrgency_handle)

    spamWords = []


    dest_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Intermediate Data/Spam Detection/My Project/Tweets containing Spam (12-04-17).csv", "wb")
    dest = csv.writer(dest_handle)

    for i in range(len(t)):
        for row in t[i]:
            for item in row:
                spamWords.append(item)

    for i in range(len(spamWords)):
        spamWords[i] = spamWords[i].replace("\xc2\xa0", "")
    spamWords.append("please buy")
    spamWords.append("on sale")
    spamWords.append("live on")


    #print (spamWords)
    count = 0
    words = []
    frame = []
    for row in src:
        for item in spamWords:
            for i in range(len(row)):
                if item in row[i]:
                    count = count + 1
                    words.append(item)
        frame.append(row)
        if count > 0:
            frame.append("1")
            frame.append(words)
        else:
            frame.append("0")
        dest.writerow(frame)
        del frame[:]
        del words[:]
        count = 0






if __name__ == "__main__":
    main()
