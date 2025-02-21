from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.additional_functions import get_duration, format_duration, conversion_utc
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits = []
    local_time_now = conversion_utc(localtime())
    for visit in Visit.objects.filter(leaved_at=None):
        non_closed_visits.append({
            'who_entered': visit.passcard,
            'entered_at': local_time_now,
            'duration': format_duration(get_duration(visit.entered_at, local_time_now)),
        })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
