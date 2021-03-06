import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import csv
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)
source_handle = open("/mnt/windows/Projects/Sentiment Analysis/usage of # to trend/CSV Files/Intermediate Data/Hydrocarbon - POS(25-07).csv", "r")
source = csv.reader(source_handle)

dest_handle = open("/mnt/windows/Projects/Sentiment Analysis/usage of # to trend/CSV Files/Intermediate Data/Hydrocarbon - Named Entity(25-07).csv", "w")
dest = csv.writer(dest_handle)



def process_content():
  try:
    for i in source:
      words = nltk.word_tokenize(str(i))
      tagged = nltk.pos_tag(words)
      namedEnt = nltk.ne_chunk(tagged, binary=True)
      dest.writerow(namedEnt)
  except Exception as e:
    print(str(e))


process_content()
