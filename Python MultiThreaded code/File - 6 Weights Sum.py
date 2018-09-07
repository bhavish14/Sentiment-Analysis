import csv
import numpy as np
import random
import multiprocessing
import os

def add_vals(file_source):
    src_handle = open('' % file_source, "r")
    src = csv.reader(src_handle)
    des_handle = open('' % file_source, "wt")
    des = csv.writer(des_handle)
    vals = list(src)
    vals.pop(0)
    des.writerow(['Sum', 'Nature of the user'])
    for row in vals:
        val = []
        t = 0
        for item in row:
            t += float(item)
        val.append(t)
        if t > 0:
            sentiment = 'Positive'
        elif t < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
        val.append(sentiment)
        des.writerow(val)


def data_handle(list):
    for item in list:
        print(item)
        add_vals(item)

#id, created, text = np.loadtxt('', delimiter=',', unpack = True, dtype='str')
#src_handle = open('', "rb")
def main():
    file_names = os.listdir(')
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
