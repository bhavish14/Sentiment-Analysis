import csv
import numpy as np
import random
import multiprocessing
import os

def tokenize(file_source):
    src_handle = open('' % file_source, "r")
    src = csv.reader(src_handle)
    des_handle = open('' % file_source, "wt")
    des = csv.writer(des_handle)

    for row in src:
        t = str(row[2]).split(" ")
        des.writerow(t)




def get_data(list):
	for item in list:
		tokenize(item)

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
        process = multiprocessing.Process(target=get_data, args=(list_names[i]))
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
