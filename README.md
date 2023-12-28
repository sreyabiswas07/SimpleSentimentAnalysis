# Simple Sentiment Analysis
This is a simple Sentiment analysis python script file for the purpose of learning.

## Steps to run this script:

- Save the file with sentiment.py
- run the command python3 ./sentiment.py

## Output

```{'neg': xxx, 'neu':yyy, 'pos': zzz, 'compound': xyz}```
<br>
<br>
Under the hood, we are using SentimentIntensityAnalyzer from NLTK Library which gives us the negetive, neutral, positive and compound value of a sentiment for a sentence/tweet. Range of compound value is -1 to 1.
