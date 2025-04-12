# extract.py
import requests
from bs4 import BeautifulSoup

def extract_imdb_data():
    url = "https://www.imdb.com/chart/top"
    headers = {
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0"
    }

    try:
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        print("First 1000 characters of the response:")
        print(response.text[:1000])  # Debug: Check if HTML is loading

        if response.status_code != 200:
            print("❌ IMDb page not reachable.")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        rows = soup.select('tbody.lister-list tr')
        print(f"Found {len(rows)} rows.")  # Debug: Check if movie rows are found

        movies = []

        for row in rows[:10]:
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
    
    except Exception as e:
        print(f"Error: {e}")
        return []
