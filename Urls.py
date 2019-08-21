from enum import Enum


class Urls(Enum):
    token = "https://www.strava.com/oauth/token"
    athlete = "https://www.strava.com/api/v3/athlete"
    get_activity = "https://www.strava.com/api/v3/activities/{0}"
    get_all_activities = "https://www.strava.com/api/v3/athlete/activities"

