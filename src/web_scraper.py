import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np

#Scrape reviews for a given airline from multiple pages and return DataFrame containing the scraped reviews.
def scrape_reviews(airline, pages, page_size):
    """
    Args:
        airline (str): Name of the airline.
        pages (int): Number of pages to scrape.
        page_size (int): Number of reviews per page.
    """

    base_url = "https://www.airlinequality.com/airline-reviews"
    reviews = pd.DataFrame()
    
#Extract review statistics from a review element.
    def extract_stats(para, airline):
        """
        Args:
            para (bs4.element.Tag): Review element.
            airline (str): Name of the airline.

        Returns:
            dict: Dictionary containing the extracted statistics.
        """

        stats = {
            "Type_Of_Traveller": 0,
            "Seat_Type": 0,
            "Route": 0,
            "Date_Flown": 0,
            "Seat_Comfort": 0,
            "Staff_Service": 0,
            "F&B": 0,
            "Inflight_Entertainment": 0,
            "Ground_Service": 0,
            "Value_For_Money": 0,
            "Recommended": 0,
            "Airlines": airline,
        }
        for par in para.find_all("tr"):
            if par.find("td", {"class": "review-rating-header type_of_traveller"}):
                ans = par.find("td", {"class": "review-value"}).get_text()
                stats["Type_Of_Traveller"] = ans
            elif par.find("td", {"class": "review-rating-header cabin_flown"}):
                ans = par.find("td", {"class": "review-value"}).get_text()
                stats["Seat_Type"] = ans
            elif par.find("td", {"class": "review-rating-header route"}):
                ans = par.find("td", {"class": "review-value"}).get_text()
                stats["Route"] = ans
            elif par.find("td", {"class": "review-rating-header date_flown"}):
                ans = par.find("td", {"class": "review-value"}).get_text()
                stats["Date_Flown"] = ans
            elif par.find("td", {"class": "review-rating-header seat_comfort"}):
                rate = len(par.find_all("span", {"class": "star fill"}))
                stats["Seat_Comfort"] = rate
            elif par.find("td", {"class": "review-rating-header cabin_staff_service"}):
                rate = len(par.find_all("span", {"class": "star fill"}))
                stats["Staff_Service"] = rate
            elif par.find("td", {"class": "review-rating-header food_and_beverages"}):
                rate = len(par.find_all("span", {"class": "star fill"}))
                stats["F&B"] = rate
            elif par.find("td", {"class": "review-rating-header inflight_entertainment"}):
                rate = len(par.find_all("span", {"class": "star fill"}))
                stats["Inflight_Entertainment"] = rate
            elif par.find("td", {"class": "review-rating-header ground_service"}):
                rate = len(par.find_all("span", {"class": "star fill"}))
                stats["Ground_Service"] = rate
            elif par.find("td", {"class": "review-rating-header value_for_money"}):
                rate = len(par.find_all("span", {"class": "star fill"}))
                stats["Value_For_Money"] = rate
            elif par.find("td", {"class": "review-rating-header recommended"}):
                ans = par.get_text()
                stats["Recommended"] = ans
        return stats
    
    # create URL to collect links from paginated data 
    for i in range(1, pages + 1):
        url = f"{base_url}/{airline}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"
        print(f"Scraping page {i}")
        response = requests.get(url)
        content = response.content
        parsed_content = BeautifulSoup(content, "html.parser")
        review_stats = parsed_content.find_all("div", {"class": "review-stats"})
        stats_list = [extract_stats(para, airline) for para in review_stats]
        reviews = reviews.append(stats_list, ignore_index=True)
        print(f"   ---> {len(reviews)} total reviews")
        time.sleep(np.random.randint(6))
    return reviews

#scrape reviews for multiple airlines and combine them into a single DataFrame.
def main():
    airlines = ["finnair", "sas-scandinavian-airlines", "swiss-international-air-lines"]
    pages = 8
    page_size = 100
    all_reviews = pd.DataFrame()

    for airline in airlines:
        print(f"{airline}:")
        airline_reviews = scrape_reviews(airline, pages, page_size)
        all_reviews = all_reviews.append(airline_reviews, ignore_index=True)

    print(f"Total reviews: {len(all_reviews)}")

if __name__ == "__main__":
    main()

