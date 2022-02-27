# Yelp-search
I created a flask app to search for restaurants on yelp

## Homework Questions

**1. Create a python function to scrape Yelp data for 50 restaurants close to you OR Craigslist for the top 50 items of any topic interesting to you. Think about what data you want to scrape aside from the name and location. You must pick at least three other fields. You can use beautiful soup, selenium, scrapy, and/or splinter as possible.**

I decided to scrape Yelp because I love food! I am always looking for new restaurants to try :) 

To complete this, I went to Yelp.com and searched for my ZIP. I right-clicked on the fields of interest and selected "inspect element" to view the html source code. The fields I ended up selecting were
1) Restaurant name
2) Neighborhood location
3) Number of stars (out of a 5-star rating)
4) Total number of reviews
5) Featured comment from customer

It was fairly simply to retrieve the restaurant name. The other fields, however, were much more challenging. For instance, not every restaurant had a location attached to it, so I had to account for this discrepancy. Some fields were also deeply burried within the html source code, and finding the proper parent element was difficult. There were also instances where I tried to print what I thought was the proper parent, but then the element I wanted would not appear underneath. In sum, it was a lot of trial and error to get it right. The most challenging element was the last. I originally tried to extract whether the restaurant was "open" or "closed." Unfortunately, this element was not available for many restaurants. I thought overall, it would not be very helpful to include. Therefore, I switched to extracting the featured comment. There were some missing comments as well, but not too many. I simply replaced the missing comments with "Not Available." 

Through the code in this repo, you can see I primarily used Beautiful Soup to complete this task. But before jumping into VSCode, I ran my program in a Jupyter notebook to more easily see how my code was working. 

Here is an example of the resulting dataframe in my Jupyter notebook.
![df_screenshot](https://user-images.githubusercontent.com/59490033/155899605-4f7a9472-9f98-4037-8fd2-ad5ca5891d79.PNG)


*Please see the yelp_function.py file in this repo for the full code.*

**2. Create a local API that calls your scrape function and stores the data when you call /scrape endpoint. The data you scrape should be viewable when you go to /all.**

To create my local API, I had to import the yelp function created in the previous step. The home page simply included directions on how to use my app.

homepage:
![homepage](https://user-images.githubusercontent.com/59490033/155899675-9de04d71-008a-448d-947b-48a70bada936.PNG)

The /scrape endpoint then called my data and stored it in a dictionary. I rendered this through an html template so that the user could see that the function was successful.

/scrape:
![pg2](https://user-images.githubusercontent.com/59490033/155899723-d004b64d-b437-4629-9e5a-05b88242ddc3.PNG)

Finally, I rendered the data into a clean table format so that the data could be more useable and more interpretable for the end user. 

/scrape/all:
![pg3](https://user-images.githubusercontent.com/59490033/155899792-eec090f1-92a9-468a-b26c-eab64189de5b.PNG)

One thing I noticed, in general, is that the class names in the html source code are different for different locations. This felt odd to me. I would have thought that the underlying source code template would be the same for any location. I am wondering how web scrapers accounts for this? For example, if I wanted to easily scrape Yelp data for 50 restaurants in the 3 zip codes nearest to me, how would I do that efficiently? Would I need to write completely different code per zip code? Would love to learn more about this!

*Please see the yelp_api.py file in this repo for the full code*

**3. What is web scraping? Why is it helpful? What does it mean for your online presence? Refence the readings and DataCamp.**

Web scraping is a method of extracting information through the source code of various websites. One can achieve this by utilizing various "tags" within the source code to search for specific names, classes, etc. and then extract the data. This can be helpful for a variety of reasons. For one, it can be a way to systematically organize data that would otherwise be scattered across pages within a website. This scattered and potentially unsctructed format can prevent analysis and data insight. However, if the data are retrieved through web-scraping, we can reformat into lists, data frames, dictionaries and other useful data sctructures. The instructor from the data camp video, for instance, completed a famous analysis on crime statistics through the use of web scraping. His team scraped data from city agencies across the country in order to create one unified visual, compiling and summarizing the data from the different cities.

Regarding my own online presence, I can pull information for different topics that interest me. For instance, in my current role, there are COVID-19 vaccination numbers scattered across various local public health agencies. The information is often posted, but infrequently in a simple and downloadable format. Webscraping could be a way for me to gather all of this information in a way that is more useful and that better explains vaccination numbers as a whole. On a personal level, I can scrape the web for things like concert tickets, online sales, and new zillow listings near me! In general, this seems to be a super useful skill that we can apply to most anything we'd like.

## Data Camp

![web scraping in python](https://user-images.githubusercontent.com/59490033/155861349-29164687-5444-4f09-b720-efd3fa7e0479.PNG)

![MongoDB1-2](https://user-images.githubusercontent.com/59490033/155895557-b994f375-be80-48d7-80e0-8f06fe534fa5.PNG)
