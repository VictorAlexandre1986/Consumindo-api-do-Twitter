# This is a sample Python script.
import tweepy as tw
import pandas as pd


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
consumer_key = '****************'
consumer_secrect ='******************'
bearer_token ='***********************'
access_token ='************************'
access_token_secret ='***************************'


cliente = tw.Client(bearer_token,consumer_key,consumer_key,access_token,access_token_secret)


dtformat = '%Y-%m-%dT%H:%M:%SZ'
from datetime import datetime, timedelta
# time = datetime.now() gives you the local time whereas time = datetime.utcnow()
# gives the local time in UTC. Hence now() may be ahead or behind which gives the
# error

time = datetime.utcnow()
start_time = time - timedelta(days=7)

# Subtracting 15 seconds because api needs end_time must be a minimum of 10
# seconds prior to the request time
end_time = time - timedelta(seconds=15)

# convert to strings


start_time=start_time.strftime(dtformat)
end_time=end_time.strftime(dtformat)

resposta=cliente.search_recent_tweets(query="BBB", max_results=100, start_time=start_time,end_time=end_time)

dados=resposta.data


for i in dados:
    linha = [0 for j in range(20)]

    texto= i.text
    if('RT' in dados):
        posicao = texto.find(':')
        texto[posicao+2:]



    print(texto)