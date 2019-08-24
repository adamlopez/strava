from StravaService import StravaService
from Urls import Urls



auth_service = StravaService()
print(auth_service.send_request(Urls.athlete))