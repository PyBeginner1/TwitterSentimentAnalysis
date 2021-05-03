from textblob import TextBlob       #Its a simple api for NLP like sentiment analysis(polarity)
import tweepy
import sys

auth = tweepy.OAuthHandler("WiSDPFG0xLQliAVSDJuVSfFYi", "YrdkOG9i7ji1HxlXd2gz7HL2jv5wX1VyR6geY1Wvj1e5awnO1M")
auth.set_access_token("1387289381912801280-RrQi1ueS7ffTZBzJC8bzeQkLMrDX3v", "0HxSKRlbmK1IqHWNULDl7bh5TX8MTCcJwrOYTC6KpjVEE")

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



