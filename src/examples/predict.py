import sys

import requests

sys.path.append("..")
from app.utils.logging import logger

API_ENDPOINT = "http://localhost:8080/predict"


def main():
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "x-user-group": "B",
    }

    # Post request to prediction endpoint.
    response = requests.post(API_ENDPOINT, headers=headers, params={"item_id": "2"})
    if response.status_code == 200:
        logger.info("Successful!")
        logger.info(response.json())
    else:
        logger.info(
            "Failed to get prediction!"
            + str(response.status_code)
            + " "
            + response.text
        )


if __name__ == "__main__":
    main()
