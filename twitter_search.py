from pattern.web import Twitter
from pattern.web import Crawler 
from pattern.web import download 
from pattern.web import plaintext 
from textblob import TextBlob

t = Twitter()
i = None
for j in range(3):
    for tweet in t.search('college', start=i, count=30):
        print tweet.id
        print tweet.name
        print tweet.text
        blob = TextBlob(plaintext(tweet.text))
        print blob.noun_phrases
        print
