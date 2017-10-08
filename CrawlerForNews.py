import requests
import re
import dateutil.parser as dp
from bs4 import BeautifulSoup
import sys

List_of_links = []
x = []
y = []
news = [[]]
Base_url = "http://www.nasdaq.com/symbol/aapl/news-headlines?page="
url_list = []

reload(sys)
sys.setdefaultencoding('utf8')

# Create a list of the news section urls of the respective companies
for i in range(1, 63):
    url_list.append(Base_url+str(i))
print url_list

# Extract the relevant news articles web links from the news section of selected companies
for urls in url_list:
    html = requests.get(urls)
    soup = BeautifulSoup(html.text, 'html.parser')  # Create a BeautifulSoup object

    # Retrieve a list of all the links and the titles for the respective links

    sub_links = soup.find_all('span', class_='fontS14px')
    sub_dates = soup.find_all('small')

    for links in sub_links:
        sp = BeautifulSoup(str(links), 'html.parser')  # first convert into a string
        y.append(sp.a.string)

    for d in sub_dates:
        t = str(d.contents)
        t = re.sub("[a-zA-Z]|['<']|['>']|['  '] ", "", t)

        try:
            dat = dp.parse(t[5:14], dayfirst=False, fuzzy=True)
            x.append(dat.date())

        except ValueError:
            print(t[5:14])


for i in range(0, len(x)):
    news.append([y[i], x[i]])
    print(news[i])
