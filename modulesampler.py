#Harshi Chalamani
import pandas as pd


fileName = '/Users/harshichalamani/desktop/PythonIO/tickerInfo.csv'

df = pd.read_csv(fileName)
maxClose = df['Close'].max()
print(maxClose)


import matplotlib.pyplot as plt
x = range(len(closingPrices))
plt.plot(x, closingPrices)
plt.show()

#Had to comment last three statements out because it was giving issues and no error with code was presented so was unsure on how to fix it.
comment = 'This is the best product I\'ve ever owned!'
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#sid = SentimentIntensityAnalyzer()
#sentimentScores = sid.polarity_scores(comment)
#print(sentimentScores['compound'])

from bs4 import BeautifulSoup
from urllib.request import urlopen
url = 'http://www.musicpriceguide.com'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
titleTags = soup.find_all(title = True)
for a in titleTags:
    print(a.get_text())






