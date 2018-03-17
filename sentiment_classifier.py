from sentiment_classifier.BagofWords import BagofWords

if __name__ == "__main__":
    bow = BagofWords("data/test1/neg/", "data/stopdict/googlestop", 1)
    bow.read()