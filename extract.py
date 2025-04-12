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
        if response.status_code != 200:
            print("❌ IMDb page not reachable.")
            return []
        
        print("HTML Length:", len(response.text))  # Check the length of the response body
        print("HTML Preview:")
        print(response.text[:1000])  # show first part of page for debugging

        soup = BeautifulSoup(response.text, 'html.parser')
        rows = soup.select('tbody.lister-list tr')

        print(f"Found rows: {len(rows)}")  # Debug check
        if not rows:
            print("❌ No rows found. Please check the selectors.")

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

# Test the function by calling it
movies = extract_imdb_data()
print(movies)
