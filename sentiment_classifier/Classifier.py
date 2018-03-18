class Classifier(object):
    def __init__(self, negdata, posdata, negvec, posvec):
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
        #  Calculate prior probabilities.
        self.priorpos = len(self.posdata) / (len(self.posdata) + len(self.negdata))
        self.priorneg = len(self.negdata) / (len(self.posdata) + len(self.negdata))
        print("Prior probability positive: %d" % self.priorpos)
        print("Prior probability negative: %d" % self.priorneg)

        #  Calculate negative likelihood/conditional probability.
        occurpos = self.occurence(self.posvec)
        self.condpos = self.condprob(occurpos)
        occurneg = self.occurence(self.negvec)
        self.condneg = self.condprob(occurneg)

    def condprob(self, occur):
        cond = []
        for i in range(len(occur)):
            cond.append((occur[i] + 1) / (sum(occur) + len(occur)))
        return cond

    def occurence(self, vec):
        occur = []
        for i in range(len(vec[0])):
            sum = 0
            for x in range(len(vec)):
                sum += vec[x][i]
            occur.append(sum)
        return occur

    #def predict(self):
