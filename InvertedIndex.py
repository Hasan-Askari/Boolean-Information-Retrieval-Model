from typing import OrderedDict
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

txtFiles = []
stopwords = ""
stemmedwords = []
dictionary = {}
OrderedDictionary = {}
ext = ".txt"

for i in range(1, 449):                                 # created a list for document filenames
    txtFiles.append(str(i) + ext)

StopwordList = open('./Boolean Information Retrieval Model/Stopword-List.txt', 'r')     # open Stopwords-List.txt

for each in StopwordList:                               #
    stopwords = stopwords + each                        # creating tokens of Stopwords
stopwords = word_tokenize(stopwords)                    #

for doc in range(0, 448):
    tokens = ""
    document = open('./Boolean Information Retrieval Model/Abstracts/' + txtFiles[doc], 'r')     #open documents

    for each in document:                                   #
        tokens = tokens + each                              # creating tokens of the documents
    tokens = word_tokenize(tokens)                          #
    
    for i in stopwords:                                     #
        i = i.lower()                                       # filtering stopwords
        if i in tokens:                                     # 
            tokens.remove(i)

    stemmer = PorterStemmer()                               # stemming tokens using PorterStemmer from nltk
    stemmedwords = [stemmer.stem(i) for i in tokens]        #

    for i in stemmedwords:                                  # 
        if i in string.punctuation:                         #
            stemmedwords.remove(i)                          # removing puctuations
        for j in i:                                         #
            if j in string.punctuation:                     #
                i = i.replace(j, "")                        #

    stemmedwords = list(dict.fromkeys(stemmedwords))        # removing duplicates by converting list into dictionary (data structures)
                                                            # and then back to list

    for i in stemmedwords:                                  # creating posting list 
        if i not in dictionary:
            dictionary[i] = []
        dictionary[i].append(doc + 1)

OrderedDictionary = OrderedDict(sorted(dictionary.items()))     # sorting dictionary using Python's OrderedDictionary

for i in OrderedDictionary.items():
    print(i)