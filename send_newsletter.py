import requests

def send_newsletter(newsletter):
    print("Sending newsletter...")
    url = "https://api.thirdpartyservice.com/send"
    payload = {
        "to": "newsletter@recipients.com",
        "subject": "Monthly Economic Newsletter",
        "body": newsletter
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_API_KEY'
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Newsletter sent successfully")
    else:
        print(f"Failed to send newsletter: {response.status_code} - {response.text}")
