import csv

def main():
    src_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Intermediate Data/Apple.csv","r", encoding = "ISO-8859-1")
    src = csv.reader(src_handle)
    #dest_handle1 = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Intermediate Data/Exp 3/CycloneDebbie - userNames(30-3).csv",'w')
    #dest1 = csv.writer(dest_handle1)
    dest_handle2 = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Intermediate Data/Apple alnum.csv","w")
    dest2 = csv.writer(dest_handle2)
    temp = []
    userNames = []
    '''
    for row in src:
        for item in range(len(row)):
            if row[item] == '@':
                userNames.append(row[item+1])
        dest1.writerow(userNames)
        del userNames[:]
    #print (userNames)
    dest_handle1.close()
    '''
    src_handle.seek(0,0)
    for row in src:
        for item in range(len(row)):
            if row[item].isalnum():
                temp.append(row[item])
        dest2.writerow(temp)
        del temp[:]

    src_handle.close()
    #dest_handle1.close()
    dest_handle2.close()

if __name__ == "__main__":
    main()
