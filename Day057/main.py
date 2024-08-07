from flask import Flask, render_template
import requests

app = Flask(__name__)

all_blogs = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

@app.route('/blog')
def get_all_blogs():
    return render_template("index.html", blogs=all_blogs)

@app.route("/blog/<int:id_blog>")
def get_individual_blog(id_blog):
    for individual_blog in all_blogs:
        if individual_blog["id"] == id_blog:
            return render_template("post.html", blog=individual_blog)
    return "Blog not found", 404

if __name__ == "__main__":
    app.run(debug=True)