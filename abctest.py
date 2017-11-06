#-*- coding:utf-8 -*-
import nltk
import random
#from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize

print ('Hello Sam')
short_pos = open('positive.txt','r').read()
short_neg = open('negative.txt','r').read()


# move this up here
all_words = []
documents = []


#  j is adject, r is adverb, and v is verb
#allowed_word_types = ["J","R","V"]
allowed_word_types = ['J']
p = ""
for p in short_pos.split('\n'):
    documents.append( (p, 'pos') )
    words = word_tokenize(p)
    print(words) 
    
print p     
    # pos = nltk.pos_tag(words)
    # for w in pos:
    #     if w[1][0] in allowed_word_types:
    #         all_words.append(w[0].lower())
