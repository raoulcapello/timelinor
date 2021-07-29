from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# from django.forms import modelformset_factory

from .models import Timeline, TimelineEvent
from .forms import (
    TimelineModelForm,
    TimelineEventModelForm,
    EventFormSet,
    EventFormSetHelper,
)


def timeline_view(request, id):
    timeline_obj = get_object_or_404(Timeline, id=id)
    timeline_events = TimelineEvent.objects.filter(
        timeline__id=timeline_obj.id
    ).order_by('-date')
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


def edit_timeline(request, id):
    """
    Render a form for adding a new timeline event.

    Additionally, render a formset with a form for each existing
    timeline event, populating each form with current data.
    """
    timeline = get_object_or_404(Timeline, id=id)
    timeline_events = TimelineEvent.objects.filter(timeline__id=id).order_by(
        '-date'
    )
    if request.method == 'POST':
        if 'add-event' in request.POST:
            # 'New Event' form was submitted
            new_event_form = TimelineEventModelForm(request.POST)  # Populate
            formset = EventFormSet(queryset=timeline_events)  # Empty form
            if new_event_form.is_valid():
                event = new_event_form.save(commit=False)
                event.timeline = timeline
                event.save()
                messages.success(request, 'Event saved!')
            else:
                # Form was invalid
                messages.error(request, 'Something went wrong.')
        else:
            # 'Update Events' formset was submitted
            new_event_form = TimelineEventModelForm()  # Empty form
            formset = EventFormSet(
                request.POST, queryset=timeline_events
            )  # Populate
            if formset.is_valid():
                formset.save()
                messages.success(request, 'Events updated!')
            else:
                # Formset invalid
                messages.error(
                    request, 'Something went wrong updating the event(s).'
                )

    else:
        # GET request
        new_event_form = TimelineEventModelForm()
        formset = EventFormSet(queryset=timeline_events)

    helper = EventFormSetHelper()

    return render(
        request,
        'timelines/edit-timeline.html',
        {
            'timeline': timeline,
            'new_event_form': new_event_form,
            'formset': formset,
            'helper': helper,
        },
    )


def delete_event(request, id):
    """
    Takes event id as a second argument.
    """
    event = get_object_or_404(TimelineEvent, id=id)
    title = event.title
    timeline_id = event.timeline_id
    event.delete()
    messages.info(request, f'Success: Event {title} deleted.')

    return redirect('timelines:edit', id=timeline_id)
