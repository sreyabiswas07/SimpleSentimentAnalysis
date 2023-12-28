import nltk

#nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

tweet1 = input("Enter your tweet:")
result1 = SentimentIntensityAnalyzer().polarity_scores(tweet1)
print(result1)

tweet2 = input("Enter your tweet:")
result2 = SentimentIntensityAnalyzer().polarity_scores(tweet2)
print(result2)

tweet3 = input("Enter your tweet:")
result3 = SentimentIntensityAnalyzer().polarity_scores(tweet3)
print(result3)

tweet4 = input("Enter your tweet:")
result4 = SentimentIntensityAnalyzer().polarity_scores(tweet4)
print(result4)

