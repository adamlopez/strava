import logging
from requests_oauthlib import OAuth2Session
import json
import os
from requests import Response
from Urls import Urls
from Logger import Logger

logger = logging.getLogger(os.path.abspath(__file__))

class StravaService:
    """Used to interface with the Strava API."""

    token_file = "Resources/token.json"
    client_id = 37935
    client_secret = '8a3b7cf400e318744daab02ba3e545d66e92890d'
    def token_saver(self, token):
        """save the refresh token."""
        with open(self.token_file, "w", encoding='utf-8') as token_file:
            json.dump(token, token_file)

    def __init__(self):
        refresh_payload = {'client_id': self.client_id, 'client_secret': self.client_secret}
        try:
            with open(self.token_file, 'r') as f:
                self.token = json.load(f)
        except IOError:
            logger.error('failed to load authentication token from JSON file.')
            quit()
        self.client = OAuth2Session(self.client_id, token=self.token, auto_refresh_url=Urls.token,
                                    auto_refresh_kwargs=refresh_payload, token_updater=self.token_saver)

    def send_request(self, request_endpoint: Urls) -> Response:
        response = self.client.get(request_endpoint.value)
        logger.info(response)
        logger.info(response.text)
        print(response.text)
        return response

