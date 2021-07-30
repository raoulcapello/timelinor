from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Timeline, TimelineEvent
from .forms import (
    TimelineModelForm,
    TimelineEventModelForm,
    EventFormSet,
    EventFormSetHelper,
)


@login_required
def timeline_view(request, id):
    timeline = get_object_or_404(Timeline, id=id)
    events = TimelineEvent.objects.filter(timeline__id=timeline.id).order_by(
        '-date'
    )
    return render(
        request,
        'timelines/view-timeline.html',
        {
            'timeline': timeline,
            'events': events,
        },
    )


@login_required
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
    timelines = Timeline.objects.filter(user=request.user).order_by('title')
    form = TimelineModelForm()
    return render(
        request,
        'timelines/view-timelines.html',
        {'timelines': timelines, 'form': form},
    )


@login_required
def edit_timeline(request, id):
    """
    Render a form for adding a new timeline event.

    Additionally, render a formset with a form for each existing
    timeline event, populating each form with current data.
    """
    timeline = get_object_or_404(Timeline, id=id)
    events = TimelineEvent.objects.filter(timeline__id=id).order_by('-date')
    if request.method == 'POST':
        if 'update-timeline-details' in request.POST:
            # Update timeline details
            timeline_details_form = TimelineModelForm(request.POST)  # Populate
            new_event_form = TimelineEventModelForm()  # Empty form
            formset = EventFormSet(queryset=events)  # Empty form
            if timeline_details_form.is_valid():
                timeline = timeline_details_form.save(commit=False)
                timeline.user = request.user
                timeline.id = id
                timeline.save()
                messages.success(request, 'Timeline details updated!')
            else:
                # Form was invalid
                messages.error(request, 'Could not update Timeline details.')
        elif 'add-event' in request.POST:
            # 'New Event' form was submitted
            timeline_details_form = TimelineModelForm(
                instance=timeline
            )  # Empty form
            new_event_form = TimelineEventModelForm(request.POST)  # Populate
            formset = EventFormSet(queryset=events)  # Empty form
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
            timeline_details_form = TimelineModelForm(
                instance=timeline
            )  # Empty form
            new_event_form = TimelineEventModelForm()  # Empty form
            formset = EventFormSet(request.POST, queryset=events)  # Populate
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
        timeline_details_form = TimelineModelForm(instance=timeline)
        new_event_form = TimelineEventModelForm()
        formset = EventFormSet(queryset=events)

    helper = EventFormSetHelper()

    return render(
        request,
        'timelines/edit-timeline.html',
        {
            'timeline': timeline,
            'timeline_details_form': timeline_details_form,
            'new_event_form': new_event_form,
            'formset': formset,
            'helper': helper,
        },
    )


@login_required
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


@login_required
def delete_timeline(request, id):
    """
    Takes timeline id as a second argument.
    """
    timeline = get_object_or_404(Timeline, id=id)
    title = timeline.title
    timeline.delete()
    messages.info(request, f'Success: Timeline {title} deleted.')

    return redirect('timelines:list')


def public_timeline_url(request, slug):
    """
    Make timeline graph available to all.
    Display timeline without requiring a user to be logged in.

    In case a user is logged in, and is viewing one of their own timelines,
    display the top menu bar, and an 'Edit' button.
    """
    timeline = get_object_or_404(Timeline, slug=slug)
    events = TimelineEvent.objects.filter(timeline__id=timeline.id).order_by(
        '-date'
    )
    return render(
        request,
        'timelines/view-timeline.html',
        {'timeline': timeline, 'events': events},
    )
