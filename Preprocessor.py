import sys
from nltk_contrib import timex
from nltk import word_tokenize, sent_tokenize
from nltk.tokenize import MWETokenizer

class Preprocessor(object):
    def __init__(self, rawTextFileName=None):
        if rawTextFileName is not None:
            self.file = open(rawTextFileName)
            #print file
        else:
            print "Need a text file!"

            
    def timexTagText(self):
        
        raw = self.file.read()
        #print raw
        #tag all temporal expressions with timex2 tags
        tagged_raw = timex.tag(raw)
 
        self.file.close()

        return word_tagged

    def tokenizeText(self):

        raw = self.file.read()
        word_tagged = word_tokenize(tagged_raw)
        
        self.file.close()

        return word_tagged


    def timexTagAndTokenizeText(self):

        raw = self.file.read()

        #tag all temporal expressions with timex2 tags
        tagged_raw = timex.tag(raw)

        #word-tokenize all tags
        word_tagged = word_tokenize(tagged_raw)

        #consolidate all broken apart Timex2 tags into single "words"
        mweTokenizer = MWETokenizer(mwes=[('<','/TIMEX2','>'),('<','TIMEX2','>')], separator='')
        word_tagged = mweTokenizer.tokenize(word_tagged)

        self.file.close()
        
        return word_tagged
