from flask import Flask, render_template
import tweepy
import config
import requests
from flask import jsonify
import json
from imdb import IMDb,IMDbError
from imdb.Person import Person


app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/movie/<title>')
def hello_name(title):
   tweet_urls = []

   auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
   auth.set_access_token(config.access_token, config.access_token_secret)
   api = tweepy.API(auth, wait_on_rate_limit=True)
   for tweet in tweepy.Cursor(api.search, q="#" + title, lang="en").items(20):
      for url in tweet.entities['urls']:
         if "twitter" in url['expanded_url']:
            tweet_urls.append(str(tweet.id))

   websites = streaming(title)
   movie_details = imdb_movie(title)
   # print(movie_details)
   return render_template('hello.html', target=json.dumps(tweet_urls), stream=websites,imdb_details=movie_details)

def streaming(title):
   movie_info = {}
   url = "https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/lookup"

   querystring = {"term":title,"country":"us"}

   headers = {
      'x-rapidapi-host': "utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com",
      'x-rapidapi-key': "43148b6118mshf09d051042ef830p18dcb1jsna96c6ad3cd3d"
      }

   response = requests.request("GET", url, headers=headers, params=querystring)
   response_dict=json.loads(response.text)
   streaming_dict={}
   for index in range(len(response_dict['results'])):
      movie_name=response_dict['results'][index]["name"]
      streaming_dict.setdefault(str(movie_name),[])
      for location in range(len(response_dict['results'][index]['locations'])):
         streaming_dict[movie_name].append(str(response_dict['results'][index]["locations"][location]['display_name']))

   for key,values in streaming_dict.items():
      streaming_dict[key]=list(set(values))
   return streaming_dict

def imdb_movie(title):
   movie_flag = 0
   cast_flag = 0
   rating_flag = 0
   plot_flag = 0
   try:
      ia = IMDb()
      movies = ia.search_movie(title)
      movie_id = movies[0].movieID

   except:
      movie_flag = cast_flag = rating_flag = plot_flag = 1

   movie = ia.get_movie(movie_id)
   ia.update(movie,info=['vote details','plot'])
   title = movie['title']
   print_string = {'Title': 'na','Ratings':0,'Synopsis':'na','Cast':'na'}

   def rating():
      try:
         ratings = movie['median']
      except:
         rating_flag = 1
         ratings = 0
      return ratings

   def story():
      try:
         plot = movie['plot'][0]
      except:
         plot_flag = 1
         plot = "na"
      return plot

   def casting():
      try:
         cast = movie['cast']
      except:
         cast_flag = 1
         cast = "na"
      return cast

   final_cast = []
   movie_rating = rating()
   movie_plot = story()
   movie_cast = casting()

   if movie_flag == 0:
      print_string['Title'] = title
   else:
      print_string['Title'] = "Oops, movie unavailable.."
   if rating_flag == 0:
      print_string['Ratings'] = movie_rating
   else:
      print_string['Ratings'] = "Ratings are unavailable"
   if plot_flag == 0:
      print_string['Synopsis'] = movie_plot.split("::")[0]
   else:
      print_string['Synopsis'] = "Plot unavailable"
   if cast_flag == 0:
      if movie_cast != "na":
         for i in movie_cast:
               final_cast.append(i['name'])
         print_string['Cast'] = final_cast[:6]
   else:
      print_string['Cast'] = "Cast unavailable"
   return print_string


if __name__ == '__main__':
   app.run(debug = True,port=3400)



from flask import Flask, render_template
import tweepy
import config
import requests
from flask import jsonify
import json
from imdb import IMDb,IMDbError
from imdb.Person import Person




app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/movie/<title>')
def hello_name(title):
   tweet_urls = []
   
   auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
   auth.set_access_token(config.access_token, config.access_token_secret)
   api = tweepy.API(auth,wait_on_rate_limit=True)
   for tweet in tweepy.Cursor(api.search,q="#"+title,lang="en").items(200):
      for url in tweet.entities['urls']:
         if "twitter" in url['expanded_url']:
            tweet_urls.append(str(tweet.id))
            # tweet_urls.append(url['expanded_url'].split('/')[-1])
            # tweet_urls.append({"url":url['expanded_url']})
   
   # return jsonify({"ids":tweet_urls})

   movie_details = imdb_movie(title)
   # print(movie_details)
   return render_template('hello.html', target = json.dumps(tweet_urls),imdb_details = movie_details)

def imdb_movie(title):
   # create an instance of the IMDb class
   # title = input("Enter movie name: ")
   movie_flag = 0
   cast_flag = 0
   rating_flag = 0
   plot_flag = 0
   try:
      ia = IMDb()
      movies = ia.search_movie(title)
      movie_id = movies[0].movieID

   except:
      movie_flag = cast_flag = rating_flag = plot_flag = 1

   movie = ia.get_movie(movie_id)
   ia.update(movie,info=['vote details','plot'])
   title = movie['title']
   print_string = {'title': 'na','rate':0,'plot':'na','cast':'na'}

   def rating():
      try:
         ratings = movie['median']
      except:
         rating_flag = 1
         ratings = 0
      return ratings

   def story():
      try:
         plot = movie['plot'][0]
      except:
         plot_flag = 1
         plot = "na"
      return plot

   def casting():       
      try:
         cast = movie['cast']
      except:
         cast_flag = 1
         cast = "na"
      return cast

   final_cast = []
   movie_rating = rating()
   movie_plot = story()
   movie_cast = casting()

   if movie_flag == 0:
      print_string['title'] = title
   else:
      print_string['title'] = "Oops, movie unavailable.."
   if rating_flag == 0:
      print_string['rate'] = movie_rating
   else:
      print_string['rate'] = "Ratings are unavailable"
   if plot_flag == 0:
      print_string['plot'] = movie_plot.split("::")[0]
   else:
      print_string['plot'] = "Plot unavailable"
   if cast_flag == 0:
      if movie_cast != "na":
         for i in movie_cast:
               final_cast.append(i['name'])
         print_string['cast'] = final_cast[:6]
   else:
      print_string['cast'] = "Cast unavailable"
   return print_string

   return render_template('hello.html', target = json.dumps(tweet_urls))


if __name__ == '__main__':
   app.run(debug = True,port=3400)
