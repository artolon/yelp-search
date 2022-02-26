#!/usr/bin/env python

from flask import Flask, render_template
from yelp_function import yelp_search
import pandas as pd

#create instance of Flask app
app = Flask(__name__)

# decorator with the scrape end point
@app.route("/scrape")
def scrape():
    pass
    

@app.route("/scrape/all")
def all():
    # call the yelp_search function that we created earlier and store the data as "df"
    df = yelp_search()
    # convert the data to a dictionary so that it easily renders in the html file
    df_dict = pd.DataFrame.to_dict(df)
    return render_template('index.html', html_page_text=df_dict)

if __name__ == "__main__":
    app.run(debug=True)

# export FLASK_APP=yelp_api
# flask run