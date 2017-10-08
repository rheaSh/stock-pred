import requests, re, sys
import dateutil.parser as dp
from bs4 import BeautifulSoup
from cStringIO import StringIO

reload(sys)
sys.setdefaultencoding('utf8')
Base_url = "http://www.nasdaq.com/symbol/aapl/news-headlines?page="
url_list = []
x = []


# Create a list of the news section urls of the respective companies
for i in range(1, 3):
    url_list.append(Base_url+str(i))
print url_list

for urls in url_list:
    html = requests.get(urls)
    soup = BeautifulSoup(html.text,'html.parser') # Create a BeautifulSoup object

    sub_dates = soup.find_all('small')

    for d in sub_dates:
        # print('d = '+str(d))
        t = str(d.contents)

        t = re.sub("[a-zA-Z]|['<']|['>']|['  '] ", "", t)

        try:
            date = dp.parse(t[5:14], dayfirst=False, fuzzy=True)
            #print(date)
            x.append(date)
        except ValueError:
            print(t[5:14])
        # #t = str(' '.join(t).split())


for t in x:
    print(t)
print(len(x))