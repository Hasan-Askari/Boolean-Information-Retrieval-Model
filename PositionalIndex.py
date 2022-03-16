from re import L
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
doc_Count = 0

for i in range(1, 10):                                 # created a list for document filenames
    txtFiles.append(str(i) + '.txt')

StopwordList = open('./Boolean Information Retrieval Model/Stopword-List.txt', 'r')     # open Stopwords-List.txt

for each in StopwordList:                               #
    stopwords = stopwords + each                        # creating tokens of Stopwords
stopwords = word_tokenize(stopwords)                    #

for doc in txtFiles:
    tokens = ""
    document = open('./Boolean Information Retrieval Model/Abstracts/' + doc, 'r')     #open documents

    for each in document:                                   #
        tokens = tokens + each                              # creating tokens of the documents
    tokens = word_tokenize(tokens)                          #
    
    stemmer = PorterStemmer()                               # stemming tokens using PorterStemmer from nltk
    stemmedwords = [stemmer.stem(i) for i in tokens]        #

    for i in stemmedwords:                                  # 
        if i in string.punctuation:                         #
            stemmedwords.remove(i)                          # removing puctuations
        for j in i:                                         #
            if j in string.punctuation:                     #
                i = i.replace(j, "")                        #
    # print('stemmedwords: ', stemmedwords)
    
    for i in stemmedwords:                                  #
        i = i.lower()                                       # filtering stopwords
        if i in stopwords:                                  # 
            stemmedwords.remove(i)
            # print(i)
    # print('filtered: ', stemmedwords)

    count = 0                                               # decides position
    for i in stemmedwords:                                  # creating posting list 
        List = []
        List.append([])
        if i not in dictionary:
            print('if: 1')
            List = [doc_Count + 1, [count]]
            print('List: ', List, 'List_Len: ', len(List), 'doc_Count: ', doc_Count)
        else:
            print('else: 1')
            List = dictionary.get(i)
            print('List: ', List, 'List_Len: ', len(List), 'doc_Count: ', doc_Count)
            if len(List) <= doc_Count*2:
                print('if: 2')
                List.extend([doc_Count + 1, [count]])
                if List[doc_Count + 1] in 
            else:
                print('else: 2')
                List[doc_Count*2 + 1].append(count)
        dictionary[i] = List
        # print(dictionary)

        count += 1
    doc_Count += 1

OrderedDictionary = OrderedDict(sorted(dictionary.items()))     # sorting dictionary using Python's OrderedDictionary

for i in OrderedDictionary.items():
    print(i)