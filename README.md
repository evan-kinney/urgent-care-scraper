# Urgent Care Scraper

## Prerequisites

- [**Python 3**](https://www.python.org)
- [**Google Maps API Key**](https://developers.google.com/maps/documentation/javascript/get-api-key)

## Setup

- Create Python virtual environment:

  ```shell
  python3 -m venv venv
  ```

- Activate Python virtual environment:

  - On Windows

    ```batch
    .\venv\Scripts\activate
    ```

  - On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

- Install dependencies to Python virtual environment:

  ```shell
  pip install -r requirements.txt
  ```

## Running

- Set Google Maps API key:

  - On Windows:

    ```batch
    set GOOGLE_MAPS_KEY=<YOUR_API_KEY>
    ```

  - On macOS/Linux:

    ```bash
    export GOOGLE_MAPS_KEY=<YOUR_API_KEY>
    ```

- Running the script:

  - On Windows:

    ```batch
    python src\main.py
    ```

  - On macOS/Linux:

    ```bash
    python src/main.py
    ```
