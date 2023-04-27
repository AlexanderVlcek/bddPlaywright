import logging

import requests


def test_rest_attempt():
    response = requests.get('https://api.github.com/events')

    logging.getLogger().info("==============" + str(response.status_code) + "==============")
    # logging.getLogger().info("==============" + str(response.json()) + "==============")
    logging.getLogger().info("==============" + str(response.headers) + "==============")
    logging.getLogger().info("==============" + str(response.headers["Content-Type"]) + "==============")
