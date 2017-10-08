import datetime
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt
import datetime as dt

openP = []
closeP = []
date = []
features = []
month = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
         'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}


def to_integer(dt_time):
    return 10000 * int(dt_time[2]) + 100 * int(dt_time[1]) + int(dt_time[0])


def organize_data():

    fi = pd.read_csv(r'FinalTable.csv', index_col=['Date'], header=0,
                     usecols=['Open', 'High', 'Low', 'Volume', 'Adj Close', 'Date', 'Sentiment'])
    x = 30
    # date[:] = fi.index.values[:]

    date1 = '02-01-2014'
    date2 = '31-12-2014'
    # mydates = pd.date_range(date1, date2)
    # mydates.strftime('%Y%m%d').tolist()
    mydates = [d.strftime('%d-%m-%Y') for d in pd.date_range('01-01-2014', '31-12-2014')]
    print mydates

    for i in mydates[:120]:
        f = []
        # i = str(i.date())
        dateS = i.split('-')

        try:
            # print fi.ix['15-01-2014']['Open']

            f.append(to_integer(dateS))
            f.append(fi.ix[i]['Open'])
            f.append(fi.ix[i]['High'])
            f.append(fi.ix[i]['Low'])
            f.append(fi.ix[i]['Volume'])
            f.append(fi.ix[i]['Sentiment'])

            date.append(to_integer(dateS))
            features.append(f)
            openP.append(fi.ix[i]['Open'])
            closeP.append(fi.ix[i]['Adj Close'])
        except KeyError:
            x += 1
            # print dateS

    return


def predict_prices(dates, prices, x):

    dates = np.reshape(dates, (len(dates), 1))
    cutoff = int(len(features)*3/4)
    training = features[:cutoff]
    test = features[cutoff:]

    mlp = MLPRegressor(solver='lbfgs', hidden_layer_sizes=(5, 5),
                       max_iter=100, random_state=1)
    mlp.fit(training, prices[:cutoff])
    testResult = mlp.predict(test)

    ax, pl = plt.subplots()
    pl.scatter(dates, prices, color='black', label='Data')
    pl.scatter(dates[cutoff:], testResult, color='red', label='Test with Sentiment')
    pl.scatter(dates[:cutoff], mlp.predict(training), color='blue', label='Training')
    pl.set_ylim(50, 100)


    avg = 0.0
    lms = 0.0
    le = len(testResult)
    for i in range(0, le):
        print testResult[i], prices[cutoff+i]
        avg += abs((testResult[i] - prices[cutoff+i])/prices[cutoff+i])
        lms += (testResult[i] - prices[cutoff+i])**2

    avg /= le
    lms /= 2
    print avg*100, lms

    plt.xlabel('Scaled Date')
    plt.ylabel('Closing Price')
    plt.legend()
    plt.show()

    return mlp.predict(x)


organize_data()
we = [20130201,	459.110001,	459.479996,	448.350021, 134871100, 1]
print len(date), len(closeP), len(we)
# With Sentiment: 4.35707049703 0.974236185172
# Without Sentiment: 2.26589677503 9.76806127775
# we = [[20170120, 120.449997, 120.449997, 119.730003, 32597900]]
predictedPrice = predict_prices(date, closeP, we)
print(predictedPrice)
