from datacenter.models import Passcard, is_visit_long, get_duration
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = get_object_or_404(Passcard, passcode=passcode)

    for item in Visit.objects.filter(passcard=passcard):
        is_visit_long(item)
        get_duration(item.entered_at, item.leaved_at)
        this_passcard_visits.append(
            {
                'entered_at': item.entered_at,
                'duration': get_duration(item.entered_at, item.leaved_at),
                'is_strange': is_visit_long(item)
            },
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
