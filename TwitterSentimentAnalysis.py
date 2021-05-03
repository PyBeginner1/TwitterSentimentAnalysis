from textblob import TextBlob       #Its a simple api for NLP like sentiment analysis(polarity)
import tweepy
import sys

auth = tweepy.OAuthHandler("customer key", "customer secret")
auth.set_access_token("api", "api secret")

api = tweepy.API(auth)

search_term='bjp'
tweet_amount = 200

#to search
tweets=tweepy.Cursor(api.search, q=search_term, lang='en').items(tweet_amount)

polarity = 0
positive = 0
neutral = 0
negative =0

for tweet in tweets:
    final_text=tweet.text.replace('RT', "")
    if final_text.startswith('@'):
        position = final_text.index(' ')
        final_text=final_text[position+2:]
    if final_text.startswith('@'):
        position = final_text.index(':')
        final_text=final_text[position+2:]
    analysis = TextBlob(final_text)         #sentiment analysis
    tweet_pol = analysis.polarity
    if tweet_pol > 0:
        positive += 1
    elif tweet_pol < 0:
        negative += 1
    else:
        neutral +=1

    polarity += analysis.polarity

print(polarity)
print(f"Positive is {positive}")
print(f"Negative is {negative}")
print(f"Neutral is {neutral}")



