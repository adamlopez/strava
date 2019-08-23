from enum import Enum


class Urls(Enum):
    token = "https://www.strava.com/oauth/token"
    athlete = "https://www.strava.com/api/v3/athlete"
    activity = "https://www.strava.com/api/v3/activities/{activity_id}"
    all_activities = "https://www.strava.com/api/v3/athlete/activities"

