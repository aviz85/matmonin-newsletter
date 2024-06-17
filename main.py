import json
import requests
import openai
from datetime import datetime, timedelta
from rss_collector import collect_titles
from ranker import rank_items
from content_fetcher import fetch_full_content
from article_finder import find_hebrew_article
from newsletter_creator import create_newsletter
from send_newsletter import send_newsletter
from item_selector import select_top_items, select_top_3

# רשימת כתובות ה-RSS
feed_urls = [
    "https://rss.jpost.com/rss/rssbankingandfinance",
    "https://rss.jpost.com/rss/rssbusinessandinnovation",
    "https://rss.jpost.com/rss/rssrealestate",
    "https://rss.jpost.com/rss/rssenergyandinfrastructure"
]

def main():
    print("Starting script...")
    
    # שלב א: איסוף כותרות מה-RSS
    print("Collecting titles from RSS feeds...")
    items = collect_titles(feed_urls)
    print(f"Collected {len(items)} items")
    
    # שלב ב: דירוג ראשוני של כתבות עם OpenAI
    print("Ranking items with OpenAI...")
    ranked_items = rank_items(items)
    print("Ranking completed")
    
    
    # שלב ג: בחירת 10 כתבות מובילות (2/3 משפחות, 1/3 עסקים)
    print("Selecting top 10 items...")
    top_items = select_top_items(ranked_items)
    print(f"Selected top 10 items")
    
    
    # שלב ד: קריאת תוכן מלא ודרגו מחדש
    print("Fetching full content for top items...")
    full_contents = fetch_full_content(top_items)
    print("Full content fetched")
    return
    print("Re-ranking items with full content...")
    final_rankings = rank_items(full_contents)
    print("Re-ranking completed")

    # שלב ה: בחירת 3 כתבות מובילות (2 למשפחות, 1 לעסקים)
    print("Selecting top 3 items...")
    top_3_items = select_top_3(final_rankings)
    print(f"Selected top 3 items")

    # שלב ו: חיפוש כתבות מקבילות בעברית
    print("Finding Hebrew articles...")
    hebrew_articles = [find_hebrew_article(item['link']) for item in top_3_items]
    print("Hebrew articles found")

    # שלב ז: יצירת ניוזלטר משולב
    print("Creating newsletter...")
    newsletter = create_newsletter(top_3_items, hebrew_articles)
    print("Newsletter created")

    # שלב ח: שליחת הניוזלטר ל-API חיצוני
    print("Sending newsletter...")
    send_newsletter(newsletter)
    print("Newsletter sent successfully")

if __name__ == '__main__':
    main()
