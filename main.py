import requests
response=requests.get("https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=1f74d119bbd14a13f7767654de8e9993&user_id=194117854%40N08&format=json&nojsoncallback=1")
print(response.json())
print(response.status_code)
