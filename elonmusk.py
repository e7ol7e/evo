from ntscraper import Nitter
scraper = Nitter(log_level=1, skip_instance_check=False)
tweets = scraper.get_tweets('elonmusk', mode='user', number=10, instance='http://nitter.privacydev.net')
for tweet in tweets['tweets']:
    print(tweet['text'])