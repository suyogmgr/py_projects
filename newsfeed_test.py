import requests


url = "https://nepalitimes.com/news.json"

def main():
    resp = requests.get(url)

    return print(resp.content)

main()