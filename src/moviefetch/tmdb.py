import os
import requests

type_map = {
  "playing": "now_playing",
  "popular": "popular",
  "top": "top_rated",
  "upcoming": "upcoming"
}

def fetch_movies(movie_type):
  endpoint = type_map.get(movie_type)

  if not endpoint:
    raise ValueError("Invalid movie type")

  api_key = os.getenv("TMDB_API_KEY")
  if not api_key:
    raise EnvironmentError("Missing TMDB_API_KEY in environment variables")

  url = f"https://api.themoviedb.org/3/movie/{endpoint}"

  response = requests.get(
    url,
    params={"api_key": api_key},
    timeout=10
  )

  response.raise_for_status()
  return response.json()