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

    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.select("tbody.lister-list tr")
    movies = []

    if not rows:
        print("❌ IMDb structure changed or no rows found.")
        return []

    for row in rows[:10]:  # Top 10 movies
        try:
            title_column = row.find("td", class_="titleColumn")
            rating_column = row.find("td", class_="ratingColumn imdbRating")
            title = title_column.a.text.strip()
            year = title_column.span.text.strip("() ")
            rating = rating_column.strong.text.strip() if rating_column.strong else "N/A"

            movies.append({
                "title": title,
                "year": year,
                "rating": rating
            })
        except Exception as e:
            print("⚠️ Skipped a row due to error:", e)
            continue

    return movies
