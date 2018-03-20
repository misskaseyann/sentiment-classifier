import os
import numpy as np
from nltk.stem import PorterStemmer


class BagofWords(object):
    def __init__(self, fp, stopfp, ngrams, stem):
        """
        Default constructur for initialization.

        :param fp: file path to director of documents being read.
        :param stopfp: stop word dictionary file path.
        :param ngrams: n-gram integer value.
        :param stem: boolean value of whether to utilize text stemming or not.
        """
        self.fp = fp
        self.stopfp = stopfp
        self.ngrams = ngrams
        self.totaldata = []
        self.vocabulary = {}
        self.wordcount = 0
        self.stem = stem

    def read(self):
        """
        Read in the documents in the file path and tokenize.
        """
        print("*  reading stop list data")
        #  Read the stop list.
        stoplist = open(self.stopfp, 'r', encoding='utf-8')
        #  Input buffer.
        stoplist = stoplist.read()
        stoplist = stoplist.split(',')

        print("*  reading data in file path")
        for filename in os.listdir(self.fp):
            #  Open the file in directory given.
            filename = self.fp + filename
            file = open(filename, 'r', encoding='utf-8')
            #  Input buffer
            file = file.read()
            #  Tokenize words.
            file = self.tokenize(file)
            #  Split words
            words = file.split(' ')
            #  If there are n-grams, then apply that. Otherwise implement stoplist.
            if self.ngrams > 1:
                words = self.stopwords(words, stoplist)
                words = self.split_ngrams(words)
            else:
                words = self.stopwords(words, stoplist)
            if self.stem == True:
                words = self.stemming(words)
            #  Add the words list to a larger list.
            self.totaldata.append(words)

        print("*  all data processed")

        print("*  making vocab")
        self.vocab()

    def stemming(self, file):
        """
        Stem the words to their base word.

        :param file: array of string data.
        :return: new array of string data.
        """
        wordsnew = []
        if self.stem == True:
            stemmer = PorterStemmer()
            for word in file:
                word = stemmer.stem(word)
                wordsnew.append(word)
        return wordsnew

    def tokenize(self, file):
        """
        Tokenize data for pre-processing.

        :param file: array of string data.
        :return: new array of string data.
        """
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
        text = text.replace('/', '')
        text = text.replace('_', ' ')
        # text = text.replace('---', ' ')
        # text = text.replace('--', ' ')
        text = text.replace('-', ' ')
        # # Remove numbers.
        # text = text.replace('0', '')
        # text = text.replace('1', '')
        # text = text.replace('2', '')
        # text = text.replace('3', '')
        # text = text.replace('4', '')
        # text = text.replace('5', '')
        # text = text.replace('6', '')
        # text = text.replace('7', '')
        # text = text.replace('8', '')
        # text = text.replace('9', '')
        #  Make all words lower case.
        text = text.lower()
        return text

    def stopwords(self, words, stoplist):
        """
        Remove stop words in data.

        :param words: string data.
        :param stoplist: stop word list dictionary.
        :return: new string data.
        """
        wordlist = words
        for word in stoplist:
            for item in wordlist:
                if item == word:
                    wordlist.remove(item)
        return wordlist

    def split_ngrams(self, words):
        """
        Split words based on number of n-grams.

        :param words: array of words.
        :return: new array of words with the specified n-grams.
        """
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
        """
        Create the vocabulary based on total data.

        :return: dictionary of vocabulary along with occerance values.
        """
        for data in self.totaldata:
            for word in data:
                if word != '':
                    self.wordcount += 1
                    if word in self.vocabulary:
                        self.vocabulary[word] += 1
                    else:
                        self.vocabulary[word] = 1
        print(self.vocabulary)

    def vectorize(self, data):
        """
        Vectorize the data into a large numpy matrix.

        :param data: string data to be vectorized.
        :return: word feature vector.
        """
        print("*  vectorizing data")
        wordvec = np.zeros((len(data), len(self.vocabulary)))
        count = 0
        keys = list(self.vocabulary.keys())
        print("size :")
        print(len(keys))
        for chunk in data:
            for word in chunk:
                if word != '':
                    wordvec[count][keys.index(word)] += 1
            count += 1
        print("word vec")
        print(wordvec)
        return wordvec

    def set_fp(self, fp):
        self.fp = fp
        self.totaldata = []

    def get_vocabulary(self):
        return self.vocabulary

    def get_wordcount(self):
        return self.wordcount

    def get_vocabsize(self):
        return len(list(self.vocabulary.keys()))

    def get_vocab_freq(self):
        return list(self.vocabulary.values())

    def get_processed_data(self):
        return self.totaldata

    def write_vocab(self, name):
        """
        Save the vocab into a text file.

        :param name: name of the text file.
        """
        f = open(name, "w+", encoding='utf-8')
        for key, value in self.vocabulary.items():
            f.write("\n" + key + ", %d" % value)
        f.close()
