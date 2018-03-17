from sentiment_classifier.BagofWords import BagofWords

if __name__ == "__main__":
    print("*  negative data processing")
    bow = BagofWords("data/test1/neg/", "data/stopdict/googlestop", 1)
    bow.read()
    negdata = bow.get_processed_data()

    bow.set_fp("data/test1/pos/")
    bow.read()
    posdata = bow.get_processed_data()

    negvec = bow.vectorize(negdata)
    posvec = bow.vectorize(posdata)