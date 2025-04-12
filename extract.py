import requests
import time
import pandas as pd

API_KEY = "32958f16314b73597c8b327e9c3b19eb"
BASE_URL = "https://api.themoviedb.org/3/movie/top_rated"

def fetch_top_250_tmdb():
    all_movies = []

    for page in range(1, 14):  # 13 pages = 260 movies
        params = {
            "api_key": API_KEY,
            "language": "en-US",
            "page": page
        }
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            for movie in data['results']:
                all_movies.append({
                    "title": movie.get("title"),
                    "id": movie.get("id"),
                    "rating": movie.get("vote_average"),
                    "vote_count": movie.get("vote_count"),
                    "popularity": movie.get("popularity"),
                    "release_date": movie.get("release_date"),
                    "overview": movie.get("overview"),
                    "original_language": movie.get("original_language")
                })
        else:
            print(f"Error fetching page {page}: {response.status_code}")
            break

        time.sleep(0.2)  # small delay between requests

    # Ensure exactly 250 rows
    return all_movies[:250]

if __name__ == "__main__":
    while True:
        print("Fetching Top 250 Movies from TMDb...")
        movies = fetch_top_250_tmdb()
        df = pd.DataFrame(movies)
        df.to_csv("top_250_tmdb.csv", index=False)
        print("Saved 250 movies to top_250_tmdb.csv ✅")

        print("Waiting 60 seconds before refreshing...\n")
        time.sleep(60)
