from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime
import datetime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def get_duration(visit, now_or_exit_time):
    visit_time = conversion_utc(visit)
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
    if visit.leaved_at != "" and get_duration(visit.entered_at, visit.leaved_at).total_seconds() > minutes * 60:
        return False
    else:
        return True
