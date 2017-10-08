import csv
import re
pos = []
neg = []
listt = []


def createNewsDataset():
    with open('NewsDataset.csv', 'wb') as csv2:
        a = csv.writer(csv2, delimiter=',')
        with open('News4.csv', 'r') as csvfile:
            sreader = csv.reader(csvfile)
            t = 10
            for row in sreader:
                if t == 0:
                    break

                x = row[2]
                x = re.sub("[^a-z|' '|',']", '', x)
                l = x.split(',')
                x = ''.join(l)
                x = re.sub("[''']", '', x)
                #print x
                l = [row[0], x]
                a.writerow(l)


def createTraining():
    with open('NewsDataset.csv', 'r') as csv2:
        sreader = csv.reader(csv2)
        for row in sreader:
            date = row[0]
            if date.startswith('2014'):
                listt.append([row[1], date])

    with open('TrainedNews2.csv', 'r') as csvf:
        rider = csv.reader(csvf)
        for row in rider:
            date = row[0]
            label = row[1]
            for i in range(0, len(listt)):
                if listt[i][1] == date:
                    listt[i][1] = label
                    break

    with open('TrainOn.csv', 'wb') as csv2:
        a = csv.writer(csv2, delimiter=',')
        for x in listt:
            a.writerow(x)

    with open('TrainOn.csv', 'r') as csvf:
        rider = csv.reader(csvf)
        t = 10
        for row in rider:
            if t == 0:
                break
            print row
            t -= 1


def addSentiment():
    f = open('FinalTable.csv', 'wb')
    toFinal = csv.writer(f)
    senti = []

    toFinal.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close', 'Sentiment'])
    with open('Classified.csv', 'r') as csv2:
        a = csv.reader(csv2)
        for row in a:
            z = 0 if row[1] == 'neg' else 1
            senti.append([row[0], z])

    with open('table.csv', 'r') as csvfile:
        sreader = csv.reader(csvfile)
        next(sreader)
        for row in sreader:
            z = 1
            for s in senti:
                date = row[0].split('-')
                dateNo = date[2]+date[1]+date[0]
                if dateNo == s[0]:
                    if s[1] == 0:
                        z = 0
            toFinal.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], z])

    f.close()

# createTraining()
addSentiment()
