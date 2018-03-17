import os


class BagofWords(object):
    def __init__(self):
        """Initial constructor."""

    def read(self, fp):
        for filename in os.listdir(fp):
            # open the file in directory given
            filename = fp + filename
            file = open(filename, 'r+', encoding='utf-8')
            # input buffer
            file = file.read()
            print("Original file:")
            print(file)
            file = self.tokenize(file)
            #  Split up the words.
            words = file.split(' ')
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

    #def stopwords(self):