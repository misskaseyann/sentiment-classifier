import os


class BagofWords(object):
    def __init__(self, fp, stopfp, ngrams):
        """Initial constructor."""
        self.fp = fp
        self.stopfp = stopfp
        self.ngrams = ngrams

    def read(self):
        #  Read the stop list.
        stoplist = open(self.stopfp, 'r+', encoding='utf-8')
        #  Input buffer.
        stoplist = stoplist.read()
        stoplist = stoplist.split(',')

        for filename in os.listdir(self.fp):
            # open the file in directory given
            filename = self.fp + filename
            file = open(filename, 'r+', encoding='utf-8')
            # input buffer
            file = file.read()
            print("Original file:")
            print(file)
            file = self.tokenize(file)
            words = file.split(' ')
            if self.ngrams > 1:
                words = self.split_ngrams(words)
            words = self.stopwords(words, stoplist)
            #  Split up the words.
            print("Modified file:")
            print(words)

    def tokenize(self, file):
        #  Remove the html tags.
        text = file.replace('<br /><br />', ' ')
        #  Remove the quotes.
        text = text.replace('\"', '')
        text = text.replace('\'', '')
        #  Remove punctuation.. etc.
        text = text.replace('.', '')
        text = text.replace(',', '')
        text = text.replace('?', '')
        text = text.replace('!', '')
        text = text.replace(';', '')
        text = text.replace(':', '')
        text = text.replace('  ', ' ')
        text = text.replace('(', '')
        text = text.replace(')', '')
        text = text.replace('*', '')
        text = text.replace('&', '')
        #  Make all words lower case.
        text = text.lower()
        return text

    def stopwords(self, words, stoplist):
        wordlist = words
        for word in stoplist:
            for item in wordlist:
                if item == word:
                    wordlist.remove(item)
        return wordlist

    def split_ngrams(self, words):
        wordsnew = []
        x = 0
        nwords = ''
        for word in words:
            if x == self.ngrams - 1:
                nwords = nwords + word
                x = x + 1
            elif x < self.ngrams:
                nwords =  nwords + word + ' '
                x = x + 1
            else:
                wordsnew.append(nwords)
                nwords = word + ' '
                x = 1
        return wordsnew