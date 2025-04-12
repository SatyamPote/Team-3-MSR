print("🔧 extract_imdb_data() is running...")
# extract.py
import requests
from bs4 import BeautifulSoup

def extract_imdb_data():
    url = "https://www.imdb.com/chart/top"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        print("HTML Preview:")
        print(response.text[:1000])  # show first part of page

        if response.status_code != 200:
            print("❌ IMDb page not reachable.")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        rows = soup.select('tbody.lister-list tr')
        print(f"Found rows: {len(rows)}")  # Debug check

        movies = []
        for row in rows[:10]:
            title_tag = row.find("td", class_="titleColumn").a
            year_tag = row.find("span", class_="secondaryInfo")
            rating_tag = row.find("td", class_="ratingColumn imdbRating").strong

            if title_tag and year_tag:
                title = title_tag.text.strip()
                year = year_tag.text.strip("() ")
                rating = rating_tag.text.strip() if rating_tag else "N/A"

                movies.append({
                    "title": title,
                    "year": year,
                    "rating": rating
                })

        return movies
    
    except Exception as e:
        print(f"Exception occurred: {e}")
        return []
