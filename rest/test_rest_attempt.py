import logging

import requests


def test_rest_attempt():
    r = requests.get('https://api.github.com/events')
    logging.getLogger().info("==============" + str(r.status_code) + "==============")
