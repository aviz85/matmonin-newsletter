def create_newsletter(top_items, hebrew_articles):
    print("Creating newsletter...")
    newsletter = "Newsletter - Economic News\n\n"
    for item, hebrew_article in zip(top_items, hebrew_articles):
        newsletter += f"Title: {item['title']}\n"
        newsletter += f"Link: {item['link']}\n"
        if hebrew_article:
            newsletter += f"Hebrew Link: {hebrew_article}\n"
        else:
            newsletter += "Hebrew Link: Not Found\n"
        newsletter += f"Description: {item['description']}\n\n"
    print("Newsletter created")
    return newsletter
