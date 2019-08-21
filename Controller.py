import os

from StravaService import StravaService
import DashboardService
from Urls import Urls
import Logger

logger = Logger.get_logger(os.path.basename(__file__)[:-3])

class Controller:
    """ Contains the control flow and data formatting to act as an interface
    between StravaService and the Dashboard views."""

    def __init__(self , **kwargs):
        self.__dict__.update(kwargs)

    def start_app(self, **kwargs):
        strava = StravaService()

        response = strava.send_request(Urls.get_all_activities)
        print(response)
        print(response.text)


if __name__ == "__main__":
    controller = Controller()
    controller.start_app()
