import nltk
import numpy as np
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer=PorterStemmer()
def tokenize(sentence):
   return nltk.word_tokenize(sentence)
 

def stem(word):
   return stemmer.stem(word.lower())
#tokenization is done here it means removing the white spaces 
a="how are you ?"
print(a)
a=tokenize(a)
print(a)

#stemming is done
words=['organise','organising','organises']
stemmed_words=[stem(w) for w in words]
print(stemmed_words)


#bag of words
def bag_of_words(tokenized_sentence,all_words):
   tokenized_sentence=[stem(w) for w in tokenized_sentence]
   bag=np.zeros(len(all_words),dtype=np.float32)
   for idx,w in enumerate(all_words):
      if w in tokenized_sentence:
         bag[idx] =1.0
   return bag
