import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

dates = []
prices = []


def organize_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))
        return


def predict_prices(dates,prices,x):
    dates = np.reshape(dates,(len(dates),1))

    svr_lin=SVR(kernel='linear', C=1e3)

    svr_lin.fit(dates,prices)

    plt.scatter(dates,prices, color='black', label='Data')
    plt.plot(dates,svr_lin.predict(dates),color='red',label='Linear Model')
    plt.xlabel('Date')
    plt.ylabel('Price')

    plt.legend()

    plt.show()

    return svr_lin.predict(x)[0]

organize_data('appl1.csv')

predictedPrice=predict_prices(dates,prices, 30)

print(predictedPrice)
