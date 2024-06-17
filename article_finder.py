import requests

def find_hebrew_article(link):
    print(f"Finding Hebrew article for link: {link}")
    query = {"q": link, "language": "hebrew"}
    response = requests.get("https://serpapi.com/search", params=query)
    if response.status_code == 200:
        results = response.json()
        if results.get('organic_results'):
            hebrew_link = results['organic_results'][0].get('link')
            print(f"Found Hebrew article: {hebrew_link}")
            return hebrew_link
    print(f"No Hebrew article found for link: {link}")
    return None
