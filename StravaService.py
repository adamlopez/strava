import logging
from requests_oauthlib import OAuth2Session
import json
import os
from requests import Response
from Urls import Urls
import Logger

logger = Logger.get_logger(os.path.basename(__file__)[:-3])


class StravaService:
    """Used to interface with the Strava API."""

    token_file = "Resources/token.json"
    client_id = 37935
    client_secret = '8a3b7cf400e318744daab02ba3e545d66e92890d'

    def __del__(self):
        """Destructor."""
        logger.info('Deleting instance of StravaService.')

    def __init__(self):
        refresh_payload = {'client_id': self.client_id, 'client_secret': self.client_secret}
        try:
            with open(self.token_file, 'r') as f:
                self.token = json.load(f)
        except IOError:
            logger.error('failed to load authentication token from JSON file.')
            quit()
        self.client = OAuth2Session(self.client_id, token=self.token, auto_refresh_url=Urls.token.value,
                                    auto_refresh_kwargs=refresh_payload, token_updater=self.token_saver)

    def token_saver(self, token):
        """save the token as a json string."""
        logger.info(f"Saving token to {self.token_file}.")
        with open(self.token_file, "w", encoding='utf-8') as token_file:
            json.dump(token, token_file)
        logger.info('token saved successfully.')

    def send_request(self, request_endpoint: Urls, **kwargs) -> Response:
        print(type(kwargs))
        url = request_endpoint.value
        # args = tuple([v for v in kwargs.values()])
        # if len(args) == 1:
        #     args = args[0]
        # url = url.format(args)
        logger.info(f"raw url")
        logger.debug(f"arguments passed to request: {kwargs}")
        url = url.format(kwargs)
        logger.info(f"formatted url: {url}")
        response = self.client.get(url)
        logger.info(response)
        logger.info(response.text)
        print(response.text)
        return response

