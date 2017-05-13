import tweepy as tw

def obtainOAuth():
    consumer_token = input("Introduce the route to consumer token file: ")
    consumer_secret = input("Introduce the route to consumer secret file: ")
    consumer_token_file = open(consumer_token,"r")
    consumer_secret_file = open(consumer_secret, "r")
    consumer_token_string = ""
    consumer_secret_string = ""
    for line in consumer_token_file:
        consumer_token_string = line
    for line in consumer_secret_file:
        consumer_secret_string = line
    auth = tw.OAuthHandler(consumer_token_string, consumer_secret_string)
    return auth
