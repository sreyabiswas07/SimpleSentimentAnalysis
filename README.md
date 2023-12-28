# Simple Sentiment Analysis
This is a simple example code for Sentiment analysis using NLTK.

## Steps to run this script:

- Clone the repository 
- Change directory to src
- Uncomment nltk download line if you are running for the first time
- Run the command python3 ./sentiment.py
- If you come across any issues, checkout the Issues section below or create an issue

## Output

```{'neg': xxx, 'neu':yyy, 'pos': zzz, 'compound': xyz}```
<br>
<br>
Under the hood, we are using SentimentIntensityAnalyzer from NLTK Library which gives us the negetive, neutral, positive and compound value of a sentiment for a sentence/tweet. Range of compound value is -1 to 1.

## Issues

1) If you get ```[nltk_data] CERTIFICATE_VERIFY_FAILED``` error while running the script, add the below piece of code after importing NLTK and downloading vader_lexicon:

```
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

```

2) Once the package vader_lexicon is downloaded, comment out the ```nltk.download('vader_lexicon')``` for subsequent script runs. 
