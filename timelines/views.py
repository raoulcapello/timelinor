from django.shortcuts import render, get_object_or_404

from .models import Timeline, TimelineEvent


def timeline(request, id):
    timeline_obj = get_object_or_404(Timeline, id=id)
    timeline_events = TimelineEvent.objects.filter(
        timeline__id=timeline_obj.id
    )
    return render(
        request,
        'timelines/view-timeline.html',
        {
            'timeline': timeline_obj,
            'timeline_events': timeline_events,
        },
    )
