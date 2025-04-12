import requests
import pandas as pd
import sqlite3
import random

# TMDb API Key (from image)
TMDB_API_KEY = "32958f16314b73597c8b327e9c3b19eb"

def fetch_tmdb_movies(total=250):
    print("Fetching data from IMDb (actually TMDb)...")
    movies = []
    page = 1
    while len(movies) < total:
        url = f"https://api.themoviedb.org/3/movie/popular"
        params = {
            "api_key": TMDB_API_KEY,
            "language": "en-US",
            "page": page
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json().get("results", [])
        movies.extend(data)
        page += 1
        if not data:  # If there's no more data
            break

    # Shuffle to simulate "change"
    random.shuffle(movies)
    return movies[:total]

def save_to_csv(movies, filename="imdb_movies.csv"):
    df = pd.DataFrame(movies)
    df.to_csv(filename, index=False)
    print(f"Data saved to CSV: {filename}")

def save_to_database(movies, db_name="movies.db"):
    conn = sqlite3.connect(db_name)
    df = pd.DataFrame(movies)
    df.to_sql("imdb_movies", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Data saved to database: {db_name}, table: imdb_movies")

def extract_imdb_data():
    movies = fetch_tmdb_movies()
    save_to_csv(movies)
    save_to_database(movies)
