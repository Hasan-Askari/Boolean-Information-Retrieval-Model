from lib2to3.pgen2 import token
from string import punctuation
from typing import OrderedDict
from matplotlib import collections
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

txtFileNum = []
stopwords = ""
filteredList = []
stemmedwords = []
dictionary = {}
OrderedDictionary = {}
ext = ".txt"

for i in range(1, 449):                                 # created a list for document filenames
    txtFileNum.append(str(i) + ext)

StopwordList = open('./Boolean Information Retrieval Model/Stopword-List.txt', 'r')     # open Stopwords-List.txt

for each in StopwordList:                               #
    stopwords = stopwords + each                        # creating tokens of Stopwords
                                                        #
stopwords = word_tokenize(stopwords)                    #
    # print(stopwords)

for doc in range(0, 448):
    tokens = ""
    document = open('./Boolean Information Retrieval Model/Abstracts/' + txtFileNum[doc], 'r')     #open documents

    for each in document:                                        #
        tokens = tokens + each                              # creating tokens of the documents
                                                            #
    tokens = word_tokenize(tokens)                          #
    # print(tokens)

    for i in tokens:                                        #
        i = i.lower()                                       # filtering stopwords
        if i not in stopwords:                              # 
            filteredList.append(i)                          # 

    stemmer = PorterStemmer()                               # stemming tokens using PorterStemmer from nltk

    stemmedwords = [stemmer.stem(i) for i in filteredList]  

    for i in stemmedwords:                                  # 
        if i in string.punctuation:                         #
            stemmedwords.remove(i)                          # removing puctuations
        for j in i:                                         #
            if j in string.punctuation:                     #
                i = i.replace(j, "")                        #

    # print("Stemmed Words = ", stemmedwords)

    stemmedwords = list(dict.fromkeys(stemmedwords))        # removing duplicates by converting list into dictionary (data structures)
    #                                                         # and then back to list
    # # print("FilteredList = ", filteredList)

    for i in stemmedwords:                                  # creating posting list 
        if i not in dictionary:
            dictionary[i] = []
        dictionary[i].append(txtFileNum[doc])

OrderedDictionary = OrderedDict(sorted(dictionary.items()))     # sorting dictionary using Python's OrderedDictionary

for i in OrderedDictionary.items():
    print(i)