import os

from StravaService import StravaService
import DashboardService
from Urls import Urls
import Logger

logger = Logger.get_logger(os.path.basename(__file__)[:-3])


class Controller:
    """ Contains the control flow and data formatting logic, acting as an interface
    between StravaService and the Dashboard views."""

    def __init__(self , **kwargs):
        self.__dict__.update(kwargs)

    def run_request_app(self, **kwargs):
        """Start an app to make requests. Only used for testing purposes."""
        running = True
        strava = StravaService()
        while running:
            menu = self.get_menu()
            request_number = int(input("Enter request number:"))
            logger.debug(f"requested option {request_number}.")
            if request_number == 1:
                response = strava.send_request(Urls.all_activities)
            elif request_number == 2:
                ip = int(input("Enter activity id:"))
                response = strava.send_request(Urls.activity, activity_id=ip)
            elif request_number == 4:
                # running = False
                break
            logger.info(f"Response: {response}")
            logger.info(f"Response value: {response.text}")

    def get_menu(self):
        menu_string = ""
        menu_string += "1. All Activities\n"
        menu_string += "2. Single activity\n"
        menu_string += "3. Athlete info\n"
        menu_string += "4. Quit"
        return menu_string


if __name__ == "__main__":
    controller = Controller()
    controller.run_request_app()
