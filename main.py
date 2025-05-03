import requests

def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        response.raise_for_status()
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        print(f"\nQuote of the Day\n\n\"{quote}\"\n\n— {author}\n")
    except requests.exceptions.RequestException as e:
        print("Error fetching quote:", e)

if __name__ == "__main__":
    get_quote()
