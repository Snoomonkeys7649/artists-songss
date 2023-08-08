import json
import requests
import sys


if len(sys.argv) !=2:
    sys.exit()
    
# itunes API source
response = requests.get("https://itunes.apple.com/search?entity=song&limit=30&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))

o = response.json()

#Finds the names of tracks made by an artist.
for result in o["results"]:
    print(result["trackName"])
