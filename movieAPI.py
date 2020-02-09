import requests
import json

url = "https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/lookup"

querystring = {"term":"irishmen","country":"us"}

headers = {
    'x-rapidapi-host': "utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com",
    'x-rapidapi-key': "43148b6118mshf09d051042ef830p18dcb1jsna96c6ad3cd3d"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
response_dict=json.loads(response.text)
output_dict={}
for index in range(len(response_dict['results'])):
    movie_name=response_dict['results'][index]["name"]
    output_dict.setdefault(str(movie_name),[])
    for location in range(len(response_dict['results'][index]['locations'])):
        output_dict[movie_name].append(str(response_dict['results'][index]["locations"][location]['display_name']))

for movie_name,platforms in output_dict.items():
    print(movie_name,platforms)