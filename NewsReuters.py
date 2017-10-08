import time, requests, re, sys, csv
import dateutil.parser as dp
from bs4 import BeautifulSoup


Base_url = "http://www.reuters.com/news/archive/apple?view=page&page="
url_list = []
List_of_links = []
x = []
y = []
news = [[]]
err = 0

reload(sys)
sys.setdefaultencoding('utf8')

myfile = open('News4.csv', 'wb')
N_writer = csv.DictWriter(myfile, fieldnames=['Date', 'News'])
N_writer.writeheader()

# Create a list of the news section urls of the respective companies
for i in range(3000, 3278):
    url_list.append(Base_url+str(i)+"&pageSize=10")

# Extract the relevant news articles web links from the news section of selected companies
for urls in url_list:
    x = []
    y = []
    flag = True

    while flag:

        try:
            html = requests.get(urls)
            flag = False

        except requests.exceptions.ConnectionError:
            print(urls)
            flag = True
            time.sleep(10)
            html = requests.get(urls)

    soup = BeautifulSoup(html.text, 'html.parser') # Create a BeautifulSoup object
    sub_links = soup.find_all('div', class_='story-content')

    news_date = {}

    for links in sub_links:

        sp = BeautifulSoup(str(links),'html.parser')  # first convert into a string
        st = str(sp.p.string)

        if type(sp) != None:
            st = st.replace('\n', ' ')
            st = st.replace('  ', ' ')

        dates = sp.find_all('span', class_="timestamp")
        dates = re.sub("[^0-9a-zA-Z]", " ", str(dates))
        try:
            dates = str(dp.parse(dates, dayfirst=False, fuzzy=True).date())

        except ValueError:
            err += 1
            continue

        if news_date.has_key(dates) and st not in list(news_date[dates]):
            news_date[dates].append(st)
        elif not news_date.has_key(dates):
            news_date[dates] = [st]

    for d in news_date.keys():
        N_writer.writerow({'Date': d, 'News': news_date[d]})

myfile.close()
print(err)

