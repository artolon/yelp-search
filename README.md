# yelp-search
flask app to search for restaurants on yelp

## Homework Questions

**1. Create a python function to scrape Yelp data for 50 restaurants close to you OR Craigslist for the top 50 items of any topic interesting to you. Think about what data you want to scrape aside from the name and location. You must pick at least three other fields. You can use beautiful soup, selenium, scrapy, and/or splinter as possible.**

Please see the yelp_function.py file in this repo for the code.

**2. Create a local API that calls your scrape function and stores the data when you call /scrape endpoint. The data you scrape should be viewable when you go to /all.**

Please see the yelp_api.py file in this repo for the code

**3. What is web scraping? Why is it helpful? What does it mean for your online presence? Refence the readings and DataCamp.**

Web scraping is a method of extracting information through the source code of various websites. One can achieve this by utilizing various "tags" within the source code to search for specific names, classes, etc. and then extract the data. This can be helpful for a variety of reasons. For one, it can be a way to systematically organize data that would otherwise be scattered across pages within a website. This scattered and potentially unsctructed format can prevent analysis and data insight. However, if the data are retrieved through web-scraping, we can reformat into lists, data frames, dictionaries and other useful data sctructures. The instructor from the data camp video, for instance, completed a famous analysis on crime statistics through the use of web scraping. His team scraped data from city agencies across the country in order to create one unified visual, compiling and summarizing the data from the different cities.

Regarding my own online presence, I can pull information for different topics that interest me. For instance, in my current role, there are COVID-19 vaccination numbers scattered across various local public health agencies. The information is often posted, but infrequently in a simple and downloadable format. Webscraping could be a way for me to gather all of this information in a way that is more useful and that better explains vaccination numbers as a whole. On a personal level, I can scrape the web for things like concert tickets, online sales, and new zillow listings near me! In general, this seems to be a super useful skill that we can apply to most anything we'd like.

## Data Camp

![web scraping in python](https://user-images.githubusercontent.com/59490033/155861349-29164687-5444-4f09-b720-efd3fa7e0479.PNG)
