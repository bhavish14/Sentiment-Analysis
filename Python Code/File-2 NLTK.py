#The .py file tokenizes and strips the tweets of stop words and stores it in another file in the /csv\ data/Intermediate\ Data folder


import csv
from nltk.tokenize import sent_tokenize, word_tokenize, TweetTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer
def main():
    t = []
    src_handle = open("/mnt/windows/Projects/Sentiment Analysis/usage of # to trend/CSV Files/Base Data/Hydrocarbon(25-07).csv", "r", encoding = "ISO-8859-1")
    src = csv.reader(src_handle)
    dest_handle = open("/mnt/windows/Projects/Sentiment Analysis/usage of # to trend/CSV Files/Intermediate Data/Hydrocarbon - NLTK(25-07).csv", "w")
    dest = csv.writer(dest_handle)
    stop_words = set(stopwords.words('english'))
    tknz = PunktSentenceTokenizer()
    for row in src:
        word_tokenized = []
        filtered_sentence = []
        word_tokenized = tknz.tokenize(row[0])
        filtered_sentence = [w for w in word_tokenized if not w in stop_words]
        dest.writerow(filtered_sentence)
        print(word_tokenized)
    dest_handle.close()
    src_handle.close()

if __name__ == "__main__":
    main()
