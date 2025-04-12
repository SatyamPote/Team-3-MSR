# extract.py
import requests
from bs4 import BeautifulSoup

def extract_imdb_data():
    url = "https://www.imdb.com/chart/top"
    headers = {
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("❌ Failed to fetch page:", response.status_code)
        return []

    soup = BeautifulSoup(response.content, 'lxml')

    rows = soup.select('tbody.lister-list tr')
    movies = []

    for row in rows[:10]:  # Top 10 movies
        title = row.find("td", class_="titleColumn").a.text.strip()
        year = row.find("span", class_="secondaryInfo").text.strip("() ")
        rating_tag = row.find("td", class_="ratingColumn imdbRating").strong
        rating = rating_tag.text.strip() if rating_tag else "N/A"

        movies.append({
            "title": title,
            "year": year,
            "rating": rating
        })

    return movies
