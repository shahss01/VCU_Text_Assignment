from pattern.web import Crawler
from pattern.web import download
from pattern.web import plaintext
from textblob import TextBlob
from pattern.web import Twitter

t = Twitter()
i = None
for j in range(3):
    for tweet in t.search('college', start=i, count=30):
        blob = TextBlob(plaintext(tweet.text))
        for sentence in blob.sentences:
            print(sentence.sentiment.polarity)
            print tweet.text
            print blob.noun_phrases