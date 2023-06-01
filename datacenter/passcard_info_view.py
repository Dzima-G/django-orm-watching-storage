from datacenter.models import Passcard
from datacenter.additional_functions import is_visit_long, get_duration, format_duration
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = get_object_or_404(Passcard, passcode=passcode)
    for visit in Visit.objects.filter(passcard=passcard):
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': format_duration(get_duration(visit.entered_at, visit.leaved_at)),
                'is_strange': is_visit_long(visit)
            },
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
