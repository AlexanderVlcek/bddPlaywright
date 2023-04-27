import logging

import requests
from assertpy import assert_that


def test_rest_attempt():
    response = requests.get('https://api.github.com/events')

    logging.getLogger().info("==============" + str(response.status_code) + "==============")
    assert_that(response.status_code).is_equal_to(200)
    # logging.getLogger().info("==============" + str(response.json()) + "==============")
    logging.getLogger().info("==============" + str(response.headers) + "==============")
    logging.getLogger().info("==============" + str(response.headers["Content-Type"]) + "==============")
