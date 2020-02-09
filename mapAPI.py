import geocoder
import tweepy
from arcgis.gis import GIS

gis = GIS()
map = gis.map("Redlands, CA")
map

#Twitter Credentials
consumer_key = 'Xsm1PSWiJYFkn0Rmoi53Mm8pU'
consumer_secret = 'DzckZZPyAKPQZdCtUWVshUhczjGMOeST53FmR1q41r2oqOWjuL'
access_token = '1082567145395937280-10ARA8VBNprf6TzT0o1QDjBojIA9oV'
access_token_secret = '0g84r99NYhYY9Pt69OYKrgr5VeBGh2X6nCAt6oHikdSKO'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
movieName="Avengers"
date="2017-04-03"
locations=[]
for tweet in tweepy.Cursor(api.search,q="#"+movieName,lang="en",since=date).items(100):
    gis = GIS()
    locations.append(tweet.user.location)
map = gis.map(locations)
print(map)