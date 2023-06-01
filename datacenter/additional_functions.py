from django.utils import timezone
import datetime
from django.utils.timezone import localtime


def get_duration(visit, now_or_exit_time):
    visit_time = conversion_utc(visit)
    if now_or_exit_time is None:
        now_or_exit_time = conversion_utc(localtime())
    now_or_exit_time = conversion_utc(now_or_exit_time)
    delta_time = now_or_exit_time - visit_time
    return delta_time


def format_duration(duration):
    formatted_time = str(datetime.timedelta(seconds=duration.total_seconds()))
    return str(formatted_time).split('.')[0]


def conversion_utc(time):
    current_time_zone = timezone.get_current_timezone()
    formatted_time = current_time_zone.normalize(time.astimezone(current_time_zone))
    return formatted_time


def is_visit_long(visit, minutes=60):
    if get_duration(visit.entered_at, visit.leaved_at).total_seconds() <= minutes * 60:
        return False
    return True
