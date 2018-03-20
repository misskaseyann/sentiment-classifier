import numpy as np


class Classifier(object):
    def __init__(self, negdata, posdata, negvec, posvec):
        """
        Default constructor.

        :param negdata: raw negative data string array.
        :param posdata: raw positive data string array.
        :param negvec: negative document feature vectors.
        :param posvec: positive document feature vectors.
        """
        #  raw data
        self.negdata = negdata
        self.negvec = negvec
        self.posdata = posdata
        self.posvec = posvec

        self.priorpos = 0
        self.priorneg = 0

        self.condpos = []
        self.condneg = []

    def learn(self):
        """
        Train the Naive Bayes algorithm for prior and conditional probabilities.
        """
        #  Calculate prior probabilities.
        self.priorpos = len(self.posdata) / (len(self.posdata) + len(self.negdata))
        self.priorneg = len(self.negdata) / (len(self.posdata) + len(self.negdata))
        print("Prior probability positive: ")
        print(self.priorpos)
        print("Prior probability negative: ")
        print(self.priorneg)

        #  Calculate negative likelihood/conditional probability.
        occurpos = self.occurence(self.posvec)
        self.condpos = self.condprob(occurpos)
        occurneg = self.occurence(self.negvec)
        self.condneg = self.condprob(occurneg)

    def condprob(self, occur):
        """
        Calculates the conditional probabilities.

        :param occur: number of occurances in feature vector.
        :return: conditional probability value.
        """
        cond = []
        for i in range(len(occur)):
            cond.append((occur[i] + 1) / (sum(occur) + len(occur)))
        return cond

    def occurence(self, vec):
        """
        Calculate the word occurence in the feature vectors.

        :param vec: matrix vectors.
        :return: occurence value.
        """
        occur = []
        for i in range(len(vec[0])):
            sum = 0
            for x in range(len(vec)):
                sum += vec[x][i]
            occur.append(sum)
        return occur

    def predict(self, docs):
        """
        Predict the documents whether they are positive or negative sentiment.

        :param docs: document feature vector data.
        :return: total count of documents, positive classifications, negative classifications.
        """
        positivecount = 0
        negativecount = 0
        doc = 0
        for i in range(len(docs)):
            predictpos = np.log(self.priorpos)
            predictneg = np.log(self.priorneg)
            for x in range(len(docs[0])):
                num = docs[i][x]
                if num != 0 and x < len(self.condpos):
                    predictpos += np.log(self.condpos[x])
                    predictneg += np.log(self.condneg[x])
            print("doc # %d" % doc)
            if predictpos > predictneg:
                positivecount += 1
                print("POSITIVE prediction")
            else:
                negativecount += 1
                print("NEGATIVE prediction")
            doc += 1
        totalcount = positivecount + negativecount
        return totalcount, positivecount, negativecount
