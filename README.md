# stock-pred
Predict the stock market prices of Apple Inc along with the sentiment analysis of news articles of the same day.

The project uses labeled data from the year 2015 to predict the stock market price of Apple stock for some days ahead, which can range either from a couple of days to a couple of months, which is modifiable in the code.
We also use Multi-Layer perceptron for prediction of the prices. For sentiment analysis, textblob's Naive Bayes classifier is employed. The features used are: date, starting price, closing price, highest price, lowest price, volume of shares traded and the sentiment (positive or negative).
The dataset we use here is the stock records of Apple Inc for a year from 2015 to 2016.
The news headlines used are scraped from the Reuters website and then preprocessed to train on a NaiveBayes classifier for emotions. 
Due to the simplicity of the sentiment analysis used, the accuracy improved without considering sentiment as a feature.
