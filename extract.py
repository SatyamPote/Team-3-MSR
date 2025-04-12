import requests
import pandas as pd
import sqlite3
from datetime import datetime
import random

API_KEY = '32958f16314b73597c8b327e9c3b19eb'

def fetch_tmdb_data():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        print("Failed to fetch data:", response.status_code)
        return []

def transform_data(raw_data):
    movies = []
    for movie in raw_data:
        movies.append({
            "id": movie["id"],
            "title": movie["title"],
            "release_date": movie["release_date"],
            "genre_ids": movie["genre_ids"],
            "vote_average": movie["vote_average"]
        })
    return movies

def save_to_csv(data):
    df = pd.DataFrame(data)

    # Shuffle to simulate changing data
    df = df.sample(frac=1).reset_index(drop=True)

    # Generate filename with current timestamp
    now = datetime.now()
    filename = f"imdb_{now.day}_D_{now.hour}_H_{now.minute}_M_{now.second}_S.csv"
    df.to_csv(filename, index=False)
    print(f"✅ Data saved to CSV: {filename}")
    return df

def save_to_database(dataframe):
    conn = sqlite3.connect("imdb_data.db")

    # Convert list columns to strings (e.g., genre_ids)
    dataframe["genre_ids"] = dataframe["genre_ids"].apply(lambda x: str(x))

    dataframe.to_sql("imdb_movies", conn, if_exists="replace", index=False)
    conn.close()

def extract_imdb_data():
    raw_data = fetch_tmdb_data()
    transformed_data = transform_data(raw_data)
    df = save_to_csv(transformed_data)
    save_to_database(df)
