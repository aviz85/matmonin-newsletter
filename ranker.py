from openai import OpenAI
import json, os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Get the API key from the environment variable
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

client = OpenAI(api_key=OPENAI_API_KEY)

def rank_items(items):
    # Attempt to read from existing file first
    if os.path.exists('first_ranking.json'):
        with open('first_ranking.json', 'r') as file:
            output = file.read()
            print("Loaded ranking from file.")
            return json.loads(output)['items']

    print("Starting to rank items...")
    documents = [{"link":item['link'], "title": item['title'], "document_content": item['description']} for item in items]
    prompt = f"""
<documents>
{json.dumps(documents, indent=2)}
</documents>
Using the data from the RSS feed, generate a JSON object for each item with the following structure:
{{
"link": "[item url]",
"title": "[item title]",
"description": "[description text]",
"relevanceForFamilies": [1-5 rating],
"relevanceForSmallBusinesses": [1-5 rating]
}}
The 1-5 ratings should assess how relevant the content is for an average Israeli family or small business, considering direct and indirect impacts. 5 is most relevant, 1 is least relevant.
Enclose the full result in the following JSON structure:
{{
"items": [
{{
"link": "[item url]",
"title": "[item title]",
"description": "[description text]",
"relevanceForFamilies": [1-5 rating],
"relevanceForSmallBusinesses": [1-5 rating]"
}},
...
]
}}
"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role":"user", "content": prompt}],
        max_tokens=4000,
        response_format={"type": "json_object"}
    )
    output = response.choices[0].message.content.strip()
    print("Finished ranking items")

    # Save to file
    with open('first_ranking.json', 'w') as file:
        file.write(output)

    return json.loads(output)['items']

