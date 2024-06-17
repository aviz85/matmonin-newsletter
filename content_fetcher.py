import requests
import json
from bs4 import BeautifulSoup

def fetch_full_content(items):
    print("Fetching full content for items...")
    full_contents = []
    for item in items:
        print(f"Fetching content for link: {item['link']}")
        response = requests.get(item['link'])
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            content = soup.get_text()
            full_contents.append({
                'link': item['link'],
                'title': item['title'],
                'description': content
            })
            print(f"Content fetched for link: {item['link']}")
        else:
            print(f"Failed to fetch content for link: {item['link']}")

    # Save the full contents to a JSON file
    with open('full_contents.json', 'w', encoding='utf-8') as f:
        json.dump(full_contents, f, ensure_ascii=False, indent=4)

    print("Finished fetching full content")
    return full_contents
