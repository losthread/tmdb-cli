from .tmdb import fetch_movies

# UI layer
def run(movie_type):
  data = fetch_movies(movie_type)

  for movie in data["results"]:
    title = movie.get("title", "N/A")
    date = movie.get("release_date", "N/A")
    rating = movie.get("vote_average", "N/A")

    print(f"{title} ({date}) ⭐ {rating}")