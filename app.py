from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import Scraping

# Set up FLask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   print(0)
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   print(1)
   mars_data = Scraping.scrape_all()
   print(2)
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   print(3)
   return redirect('/', code=302)

if __name__ == "__main__":
   app.run(debug=True)