# Customer Reviews and Sentiment Analysis to Uncover Findings for Top10 European Airlines 

<p align="center">
<img src="https://github.com/celiaXH/airline_reviews_analysis/blob/main/input/cover.jpg" width="718" height="501">
</p>

## Project Overview
* Azure were used to host web scraper for over 10,000 reviews from website Skytrax from 2014 to nowadays. 
* Reviews data including seat comfort, food&Beverage, inflight entertainment and recommendation etc. were  
  cleaned and performed EDA.
* To conduct sentimetnt analysis on comment, I used lexicon-based approaches with VADER.
* The final result wewe demostrated and visualization as a Power BI report.
   
## Motivation
The customer feedback analysis project offers an exciting opportunity to make a tangible impact for airline companies who aiming at enhance customer satisfaction, drive innovation, and contribute reputation. It is also a project that combines analytical skills and data visualization with the ability to influence key decisions, fostering personal and professional growth while creating a positive impact on both the company and its customers.

## Tools and Requirements
**Python Version:** 3.9.7 <br />
**Microsoft Power BI and An Azure Account:** It' free to set it up at azure.microsoft.com <br />
**Requirements:** ```pip install -r requirements.txt```

## Web Scraping In Azure Function
Built a **web scraper** using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to scrape 10,000  reviews for each airlines from [skytrax](https://www.airlinequality.com/), an Airline rewiew website.For each review, I retrieved the following top 10 Airlines in Europe based on [List of largest airlines in Europe](https://en.wikipedia.org/wiki/List_of_largest_airlines_in_Europe):
* Lufthansa
* Turkish-Airlines 2310
* Air France 1254
* British Airways
* KL-royal-dutch-airlines 1477
* Finnair 800
* Swiss swiss-international-air-lines 900
* SAS Group 800
* EasyJet easyjet 1000
* Ryanair  1000

## Data Cleaning and Preprocessing
* The imputation of key satisfaction factors(which is rate max of 5) were taken by spliting two groups(Top8, and low cost airlines).   
* Flight route were parsed to departure point and destination point.

## Sentiment Analysis 
NLTK is a useful platform for Python to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries.
This is the the analying steps:
* Cleaning the text: Removed all special characters and numericals leaving the alphabets.
* Tokenization 
* Enrichment – POS tagging
* Stopwords removal
* Obtaining the stem words(lemmatization)
* Sentiment Analysis using **VADER**: **VADER** stands for Valence Aware Dictionary and Sentiment Reasoner. It not only tells if the statement is positive or negative also along with the intensity of emotion.
if the intensity of emotion is >0.5 then considered as positive; <0.5 considered as negative and else will be neutral.

## Visual Representation
Power BI report were created and shared on a [link](https://app.powerbi.com/reportEmbed?reportId=d3d41c42-ab3e-4e00-a11c-1d9e55857896&autoAuth=true&ctid=1c379a3a-481a-418c-8757-972127fcaa7f) to present the distribution of reviews and the comparision between airlines.
Here are some interesting insights I found:
* The average positive sentiment rate is 45% for Top10 Airlines 
* Air France has highest reputation with 57.9% of positive commend and mainly from single travelers.

<p align="center">
<img src="https://github.com/celiaXH/airline_reviews_analysis/blob/main/input/slides_1.jpg" width="718" height="501">
</p>

<p align="center">
<img src="https://github.com/celiaXH/airline_reviews_analysis/blob/main/input/slides_2.jpg" width="718" height="501">
</p>


