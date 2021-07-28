from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Timeline, TimelineEvent
from .forms import TimelineModelForm


def timeline_view(request, id):
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


def timeline_list_view(request):
    if request.method == 'POST':
        form = TimelineModelForm(request.POST)
        if form.is_valid():
            timeline = form.save(commit=False)
            timeline.user = request.user
            timeline.save()
            messages.success(request, 'Timeline saved.')
        else:
            messages.error(request, 'Something went wrong.')
    timelines = Timeline.objects.filter(user=request.user)
    form = TimelineModelForm()
    return render(
        request,
        'timelines/view-timelines.html',
        {'timelines': timelines, 'form': form},
    )
