# extract.py
import requests
from bs4 import BeautifulSoup

def extract_imdb_data():
    url = "https://www.imdb.com/chart/top"
    headers = {"Accept-Language": "en-US,en;q=0.5"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.select('tbody.lister-list tr')
    movies = []

    for row in rows[:10]:  # Top 10 movies
        title = row.find("td", class_="titleColumn").a.text.strip()
        year = row.find("span", class_="secondaryInfo").text.strip("() ")
        rating = row.find("td", class_="ratingColumn imdbRating").strong
        rating = rating.text.strip() if rating else "N/A"

        movies.append({
            "title": title,
            "year": year,
            "rating": rating
        })

    return movies
