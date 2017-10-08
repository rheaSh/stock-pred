import csv
from textblob.classifiers import NaiveBayesClassifier
import pickle

train = []


def Make_Classifier():
    global train
    cl = NaiveBayesClassifier(train)

    f = open('my_classifier.pickle', 'wb')
    pickle.dump(cl, f)
    f.close()


def Classify():

    f = open('my_classifier.pickle', 'rb')
    cla = pickle.load(f)
    f.close()

    f2 = open('Classified', 'wb')
    riter = csv.writer(f2, delimiter=',')

    print(cla.classify("despite three failed raids free hostages held militants united states continue"
                       " conduct operations officials indicated sunday president barack obama grapples"
                       " spate kidnappings killings american citizens"))  # "neg"

    with open('NewsDataset.csv', 'r') as csv2:
        sreader = csv.reader(csv2)
        for row in sreader:
            label = cla.classify(row[1])
            riter.writerow([row[0], label])

    f2.close()
    cla.show_informative_features()
    print (cla.accuracy(train))


def getDataSet():
    with open('TrainOn.csv', 'r') as csvfile:
        rider = csv.reader(csvfile)
        t = 10
        for row in rider:
            if t == 0:
                break
            train.append(tuple((row[0], row[1])))

# Make_Classifier()
Classify()
