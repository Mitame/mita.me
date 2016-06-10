from . import app

from flask import render_template, url_for

navbar_links = []
app.add_template_global(navbar_links, "navbar_links")




@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about", navbar_title="Home")
def about():
    return render_template("about.html")


@app.route("/hire", navbar_title="Hire me")
def hire():
    return render_template("hire.html")

navbar_links.extend([
    {
        "text": "About",
        "href": "/about",
    },
    {
        "text": "Hire me!",
        "href": "/about",
    }
])
