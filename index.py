from flask import Flask, Response
from flask_limiter import Limiter
import requests, random, time

app = Flask(__name__)

Limiter(app, key_func=lambda: "global", default_limits=["5 per second"])

def get_dog():
    time.sleep(0.2)
    return requests.get("https://dog.ceo/api/breeds/image/random").json()["message"]

def get_cat():
    time.sleep(0.2)
    return requests.get("https://api.thecatapi.com/v1/images/search").json()[0]["url"]

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_image(path):
    path = path.lower()
    if path == "dog":
        url = get_dog()
    elif path == "cat":
        url = get_cat()
    else:
        url = random.choice([get_dog(), get_cat()])
    return Response(url, mimetype="text/plain")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

