from extract import fetch_top_250_tmdb
import pandas as pd

if __name__ == "__main__":
    print("Extracting data using IMDb API...")
    movies = fetch_top_250_tmdb()
    df = pd.DataFrame(movies)
    df.to_csv("top_250_imdb.csv", index=False)
    print("Data saved to top_250_imdb.csv ✅")
