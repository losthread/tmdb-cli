# TMDB CLI Tool 🎬
This is a minimal CLI tool written using python and tmdb api, that fetches movies' and series' info.

## Configuration
Before using the tool, you need to provide your TMDB API Key. You can get one for free at [themoviedb.org].
Set your API key as an environment variable in .env

## Installation
```bash
python -m venv venv
source venv/bin/activate # mac or linux
pip install tmdb-losthread
tmdb
```
If you have multiple python versions
```bash
pip3 install tmdb-losthread
```
If dependancies conflict
```bash
pip install tmdb-losthread --upgrade
```

## Usage
```bash
tmdb-app --type "playing"
tmdb-app --type "popular"
tmdb-app --type "top"
tmdb-app --type "upcoming"
```

### License
MIT

### Project reference url
[https://roadmap.sh/projects/tmdb-cli]