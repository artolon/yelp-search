#!/usr/bin/env python

from flask import Flask, render_template
from yelp_function import yelp_search
import pandas as pd

#create instance of Flask app
app = Flask(__name__)

# decorator with home end point
@app.route("/")
def home():
    text = "This is the home page. Use the endpoint /scrape to scrape restaurants from Yelp. Use scrape/all to see results!"
    caution = "Please be patient. These pages take a long time to load!"
    return render_template('homepage.html', home_text=text, caution_text=caution)

# decorator with the scrape end point
@app.route("/scrape")
def scrape():
    # call the yelp_search function that we created earlier and store the data as "df"
    df = yelp_search()
    # convert the data to a dictionary so that it easily renders in the html file
    df_dict = pd.DataFrame.to_dict(df)
    return render_template('scrape.html', html_page_text=df_dict)
    

@app.route("/scrape/all")
def all():
    df = yelp_search() 
    # place data in easy and readable format
    return df.to_html(header="true", table_id="table")

if __name__ == "__main__":
    app.run(debug=True)

# export FLASK_APP=yelp_api
# flask run