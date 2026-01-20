import pprint
from typing import Callable, Final

import dotenv
import requests

OMDB_KEY: Final[str | None] = dotenv.dotenv_values(".env")["OMDB_KEY"]
OMDB_URL: Final[str] = "https://www.omdbapi.com/"
HTTP_SUCCESS: Final[int] = 200


def cache_movie(func: Callable) -> Callable:
    """Decorator that caches movie data retrival function results
    to avoid redundant API calls.

    Args:
        func: The movie retrival to be decorated. Must accept a movie title
              parameter.

    Returns:
        The wrapper function that implements caching logic.
    """
    # Store data returned from Network API calls
    # Key is movie title, value is the movie metadata
    movie_cache = {}

    def caching_wrapper(title: str) -> dict:
        """Wrapper function that checks cache before calling the decorated function.

        Args:
            title: The title of the movie to retrieve data for.

        Returns:
            A dictionary containing movie data from cache or API call,
            or None if not found.
        """
        if title in movie_cache:
            return movie_cache[title]

        result = func(title)

        if result is not None:
            movie_cache[title] = result

        return result

    return caching_wrapper


@cache_movie
def get_movie_data(title: str) -> dict | None:
    """Retrieves movie data from the OMDB API.

    https://www.omdbapi.com/

    Args:
        title: The title of the movie to search for.

    Returns:
        A dictionary containing movie data if found, None otherwise.
    """

    request = (
        f"{OMDB_URL}?t=" + requests.utils.quote(f'"{title}"') + f"&apikey={OMDB_KEY}"
    )
    movie_response = requests.get(request)
    if movie_response.status_code == HTTP_SUCCESS:
        return movie_response.json()
    else:
        return None


def main():
    """Main function that demonstrates fetching and caching movie data.

    Fetches data for the top 5 IMDB movies twice to demonstrate the caching
    functionality. The second iteration should use cached data instead of
    making new API calls.
    """
    # From https://www.imdb.com/chart/top/
    top_five = [
        "The Shawshank Redemption",
        "The Godfather",
        "The Dark Knight",
        "The Godfather Part II",
        "12 Angry Men",
    ]

    for movie in top_five:
        pprint.pp(get_movie_data(movie))
        print("\n")

    for movie in top_five:
        pprint.pp(get_movie_data(movie))
        print("\n")


if __name__ == "__main__":
    main()
