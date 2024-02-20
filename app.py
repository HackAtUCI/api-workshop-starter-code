from flask import Flask, render_template
import requests

app = Flask(__name__)

key_header = {
    "x-api-key": ""
}
api_url = "https://api.thecatapi.com/v1/images/search?has_breeds=1"


@app.route("/")
def home():
    raw_resp = requests.get(
        api_url,
        headers=key_header,
    )
    resp = raw_resp.json()
    cat_info = resp[0]["breeds"][0]

    return render_template(
        "home.html",
        name=cat_info["name"],
        description=cat_info["description"],
        img_url=resp[0]["url"],
    )
