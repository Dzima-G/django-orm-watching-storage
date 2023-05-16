from datacenter.models import Passcard
from datacenter.models import Visit, get_duration, format_duration, conversion_utc
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits = []
    for item in Visit.objects.filter(leaved_at=None):
        local_time_now = conversion_utc(localtime())
        non_closed_visits.append({
            'who_entered': item.passcard,
            'entered_at': local_time_now,
            'duration': format_duration(get_duration(item.entered_at, local_time_now)),
        })
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
