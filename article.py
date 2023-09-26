import requests
from bs4 import BeautifulSoup

def get_article(word):
    
    wort = word.capitalize()
    
    urls = [
        f"https://der-artikel.de/der/{wort}.html",
        f"https://der-artikel.de/die/{wort}.html",
        f"https://der-artikel.de/das/{wort}.html"
    ]

    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            artikel = soup.find("span", style="color:red;")
            if artikel is not None:
                return artikel.text.strip()
    
    return None

wort = input("Bir kelime girin: ")

artikel = get_article(wort)

if artikel is not None:
    print(f"{wort} the article of the word: {artikel}")
else:
    print("Make sure you enter the correct word.")
