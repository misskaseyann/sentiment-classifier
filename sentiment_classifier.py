from sentiment_classifier.BagofWords import BagofWords

if __name__ == "__main__":
    bow = BagofWords()
    bow.read("data/test1/neg/")