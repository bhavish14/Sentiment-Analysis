import csv
import numpy as np

def main():
    t = ' '
    src_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Intermediate Data/Exp 3/CycloneDebbie - userNames(30-3).csv","r")
    src = csv.reader(src_handle)
    dest_handle = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Intermediate Data/Exp 3/CycloneDebbie - Distinct - userNames(30-3).csv",'w')
    dest = csv.writer(dest_handle)
    #src_handle1 = open("/mnt/windows/Repository/Sentiment Analysis/Csv Files/Base Data/Trump RT Cols.csv",'r')
    #src1 = csv.reader(src_handle1)


    userNames = []
    for row in src:
        for item in row:
            if not(item in userNames):
                userNames.append(item)
                dest.writerow([item])
    '''
    for row in src1:
        if not(row[2] in userNames):
            userNames.append(row[2])
            dest.writerow([row[2]])
    '''

#    print (userNames)
    src_handle.close()
    src_handle1.close()
    dest_handle.close()

if __name__ == "__main__":
    main()
