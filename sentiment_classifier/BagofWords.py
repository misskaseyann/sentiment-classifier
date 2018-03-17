import os


class BagofWords(object):
    def __init__(self, fp, stopfp, ngrams):
        self.fp = fp
        self.stopfp = stopfp
        self.ngrams = ngrams
        self.totaldata = []
        self.vocabulary = {}
        self.wordcount = 0

    def read(self):
        print("*  reading stop list data")
        #  Read the stop list.
        stoplist = open(self.stopfp, 'r+', encoding='utf-8')
        #  Input buffer.
        stoplist = stoplist.read()
        stoplist = stoplist.split(',')

        print("*  reading data in file path")
        for filename in os.listdir(self.fp):
            #  Open the file in directory given.
            filename = self.fp + filename
            file = open(filename, 'r+', encoding='utf-8')
            #  Input buffer
            file = file.read()
            #  Tokenize words.
            file = self.tokenize(file)
            #  Split words
            words = file.split(' ')
            #  If there are n-grams, then apply that. Otherwise implement stoplist.
            if self.ngrams > 1:
                words = self.split_ngrams(words)
            else:
                words = self.stopwords(words, stoplist)
            #  Add the words list to a larger list.
            self.totaldata.append(words)

        print("*  all data processed.")

        print("*  making vocab.")
        self.vocab()
        print("* done with vocab.")

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
                x += 1
            elif x < self.ngrams:
                nwords =  nwords + word + ' '
                x += 1
            else:
                wordsnew.append(nwords)
                nwords = word + ' '
                x = 1
        return wordsnew

    def vocab(self):
        for data in self.totaldata:
            for word in data:
                self.wordcount += 1
                if word in self.vocabulary:
                    self.vocabulary[word] += 1
                else:
                    self.vocabulary[word] = 1

    def reset(self, fp, stopfp, ngrams):
        self.fp = fp
        self.stopfp = stopfp
        self.ngrams = ngrams
        self.totaldata = []
        self.vocabulary = {}
        self.wordcount = 0

    def get_vocabulary(self):
        return self.vocabulary

    def get_wordcount(self):
        return self.vocabulary
