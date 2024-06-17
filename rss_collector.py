import feedparser
from datetime import datetime, timedelta

def is_last_month(date_str):
    pub_date = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %Z')
    first_of_last_month = datetime.today().replace(day=1) - timedelta(days=1)
    first_of_last_month = first_of_last_month.replace(day=1)
    end_of_last_month = datetime.today().replace(day=1) - timedelta(days=1)
    return first_of_last_month <= pub_date <= end_of_last_month

def collect_titles(feed_urls):
    print("Starting to collect titles...")
    items = []
    for url in feed_urls:
        print(f"Parsing feed: {url}")
        feed = feedparser.parse(url)
        for entry in feed.entries:
            if is_last_month(entry.published):
                items.append({
                    'title': entry.title,
                    'link': entry.link,
                    'description': entry.description
                })
                print(f"{entry.link} : {entry.title}")  # Add this line to print the title
    print("Finished collecting titles")
    
    return items
