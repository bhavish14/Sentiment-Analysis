import csv
import numpy as np
import random
import multiprocessing
import os





def add_vals(file_source):
    src_handle = open('' % file_source, "r")
    src = csv.reader(src_handle)
    des_handle = open('', "a")
    des = csv.writer(des_handle)

    vals = list(src)
    vals.pop(0)
    positive = 0
    negative = 0
    neutral = 0
    val = []
    val.append(file_source[:-11])
    for row in vals:
        if row[1] == 'Positive':
            positive += 1
        elif row[1] == 'Negative':
            negative += 1
        elif row[1] == 'Neutral':
            neutral += 1
    val.append(positive)
    val.append(neutral)
    val.append(neutral)
    val.append(positive+ negative+ neutral)
    print(val)
    des.writerow(val)
    des_handle.close()
    src_handle.close()


def data_handle(list):
    for item in list:
        add_vals(item)



#id, created, text = np.loadtxt('', delimiter=',', unpack = True, dtype='str')
#src_handle = open('', "rb")
def main():
    des_handle = open('', "a")
    des = csv.writer(des_handle)
    des.writerow(['Username', 'Positive Tweets', 'Negative Tweets', 'Neutral Tweets', 'Total Tweets'])
    des_handle.close()
    file_names = os.listdir('')
    procs = 8
    list_names = []
    length = int(len(file_names)/8)
    for t in range(8):
        temp = []
        temp.append(file_names[(t * int(len(file_names)/8)):((t + 1) * int(len(file_names)/8))])
        list_names.append(temp)

    jobs = []
    for i in range(0, procs):
        out_list = list()
        process = multiprocessing.Process(target=data_handle, args=(list_names[i]))
        jobs.append(process)

    # Start the processes (i.e. calculate the random number lists)
    for j in jobs:
        j.start()

    # Ensure all of the processes have finished
    for j in jobs:
        j.join()

    print ("List processing complete.")




if __name__ == '__main__':
    main()
