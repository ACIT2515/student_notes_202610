# REST Client Demo

A Python demonstration project that fetches movie data from the OMDB API with
caching functionality.

When run the module retrieves movie data from an open online movie database,
caching the results so that future requests for the same movie are retrieved
from a cache

## Prerequisites

- Python 3.14 or higher

## Setup

### 1. Install UV

UV is a fast Python package installer and resolver.

**Windows (PowerShell):**

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

For more installation options, see
[UV documentation](https://docs.astral.sh/uv/).

### 2. Install Dependencies

```bash
uv sync
```

### 3. Get OMDB API Key

1. Visit
   [https://www.omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx)
2. Select the FREE tier (1,000 daily requests)
3. Enter your email address
4. Check your email and click the activation link
5. Copy your API key

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```bash
OMDB_KEY=your_api_key_here
```

Replace `your_api_key_here` with the API key you received from OMDB.

## Running the Project

```bash
uv run main.py
```

The program will fetch data for the top 5 IMDB movies twice. The second
iteration uses cached data to avoid redundant API calls.

## External Libraries

### requests

[Documentation](https://requests.readthedocs.io/en/latest/)

A simple and elegant HTTP library for Python. Used to make API calls to the OMDB
service.

**Purpose in this project:**

- Makes GET requests to the OMDB API
- Handles URL encoding for movie titles
- Processes HTTP responses and status codes

### python-dotenv

[Documentation](https://saurabh-kumar.com/python-dotenv/)

Reads key-value pairs from a `.env` file and sets them as environment variables.

**Purpose in this project:**

- Securely stores the OMDB API key outside of source code
- Loads the API key at runtime from the `.env` file
- Prevents accidental exposure of sensitive credentials in version control

## Resources

### Tools

- [UV Package Manager](https://docs.astral.sh/uv/)

### Data Sources

- [OMDB API](https://www.omdbapi.com/)

### Libraries

- [Requests](https://requests.readthedocs.io/en/latest/)
- [Python-dotenv](https://saurabh-kumar.com/python-dotenv/)
