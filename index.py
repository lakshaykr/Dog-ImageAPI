from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')
def home():
    res = requests.get("https://dog.ceo/api/breeds/image/random")
    image_url = res.json()["message"]
    return Response(image_url, mimetype="text/plain")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
