import requests

def fetch_from_api():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    data = []

    for user in users:
        data.append({
            "name": user["name"],
            "website": user["website"],
            "location": user["address"]["city"]
        })

    return data