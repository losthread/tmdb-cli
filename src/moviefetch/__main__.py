from argparse import ArgumentParser
from dotenv import load_dotenv
from .cli import run

load_dotenv()

def main():
  parser = ArgumentParser()

  parser.add_argument(
    "-t", "--type",
    choices=["playing", "popular", "top", "upcoming"],
    required=True,
    help="Type of movies"
  )

  args = parser.parse_args()

  try:
    run(args.type)
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()