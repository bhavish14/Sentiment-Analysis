import csv
def main():
  src_handle = open("/mnt/windows/Projects/Sentiment Analysis/usage of # to trend/CSV Files/Base Data/#SamjhautaSecretTape Tokenized(25-7).csv", "rb")
  src = csv.reader(src_handle)
  src_handle1 = open("/mnt/windows/Projects/Sentiment Analysis/usage of # to trend/CSV Files/Base Data/#SamjhautaSecretTape(25-7).csv", "rb")
  src1 = list(csv.reader(src_handle1))
  des_handle = open("/mnt/windows/Projects/Sentiment Analysis/usage of # to trend/CSV Files/Base Data/#SamjhautaSecretTape Hash(25-07).csv", "wt")
  dest = csv.writer(des_handle)
  pos = 0
  for row in src:
    temp = []
    temp.append(str(src1[pos]))
    pos += 1
    for column in row:
      #print (column)
      if '#' in column:
        print (column)
        temp.append(str(column))
    dest.writerow(temp)

if __name__ == '__main__':
  main()
