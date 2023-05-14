from bs4 import BeautifulSoup
import requests

BASE_URL = "https://www.billboard.com/charts/hot-100/"


def scrape_top_song_titles(date_to_travel):
    resource = requests.get(f"{BASE_URL}{date_to_travel}")
    web_page = resource.text
    soup = BeautifulSoup(web_page, 'html.parser')

    song_names_spans = soup.select("li ul li h3")

    return [tag.getText().strip() for tag in song_names_spans]
