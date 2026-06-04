# note: it's literally the same style as music ms (after all it's just connection)

import time

from flask import Flask, render_template, request
from flask import send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("ImageGalleryTester.html")

@app.route("/connection.js")
def connection_js():
    return send_from_directory("templates", "connection.js")

@app.route("/images/<name>")
def image_getter(name):
    return send_from_directory("images", name)

@app.route("/gallery", methods=["POST"])
def gallery_manager():
    data = request.get_json() # retireved from connect.js
    action = data["action"]
    title = data["title"]
    request_id = data["request_id"] # now, every previous request logged will have a different id attributes, allowing for repeated click of the same button...

    with open("request.txt", "w") as f: # return the selected song back
        f.write(f"action={action}\n")
        f.write(f"title={title}\n")
        f.write(f"request_id={request_id}") 

    # the display will then hold the final image path for the gallery
    time.sleep(0.2) # slightly sloweer than the ms itself, just to play it safe (response don't overlap or glitches)
    with open("response.txt", "r") as f:
        display = f.read().strip()
    return display

if __name__ == "__main__":
    app.run(debug=True)