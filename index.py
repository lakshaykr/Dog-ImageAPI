from flask import Flask, Response
import requests
import random
import time

app = Flask(__name__)

def get_dog_image():
    time.sleep(0.2)
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    return response.json()["message"]

def get_cat_image():
    time.sleep(0.2)
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    return response.json()[0]["url"]

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_image(path):
    path = path.strip().lower()

    if path == "dog":
        image_url = get_dog_image()
    elif path == "cat":
        image_url = get_cat_image()
    else:
        image_url = random.choice([get_dog_image(), get_cat_image()])


    return Response(image_url, mimetype="text/plain")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    return Response(image_url, mimetype="text/plain")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
