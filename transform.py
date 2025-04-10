# transform.py
def transform_movies_data(data):
    transformed = []
    for movie in data:
        transformed.append({
            "Title": movie['title'],
            "Year": int(movie['year']),
            "Rating": float(movie['rating']) if movie['rating'] != 'N/A' else None
        })
    return transformed
