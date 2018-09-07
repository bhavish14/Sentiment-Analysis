import csv
def main():
    frame = []
    src_handle = open("/mnt/windows/Projects/Sentiment Analysis/usage of # to trend/CSV Files/Base Data/#SamjhautaSecretTape(25-7).csv", "rb")
    src = csv.reader(src_handle)
    des_handle = open("/mnt/windows/Projects/Sentiment Analysis/usage of # to trend/CSV Files/Base Data/#SamjhautaSecretTape Tokenized(25-7).csv", "wt")
    des = csv.writer(des_handle)

    for row in src:
        t = str(row).split(" ")
        des.writerow(t)


if __name__ == "__main__":
    main()
