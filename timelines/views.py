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
    # Initialize form
    form = TimelineModelForm()

    if request.method == 'POST':
        form = TimelineModelForm(request.POST)
        if form.is_valid():
            timeline = form.save(commit=False)
            timeline.user = request.user
            timeline.save()
            request.session['timeline_count'] = Timeline.objects.filter(
                user=request.user
            ).count()  # Update sidebar menu counter
            messages.success(request, 'Timeline saved.')
        else:
            messages.error(request, 'Something went wrong.')

    timelines = Timeline.objects.filter(user=request.user).order_by('title')

    return render(
        request,
        'timelines/view-timelines.html',
        {'timelines': timelines, 'form': form},
    )


@login_required
def edit_timeline(request, id):
    """
    Renders a:

    1) Form for adding a new timeline.

    2) Form for adding a new timeline event.

    3) Formset for previously created timeline events, rendering a form per
       event, populating each form with current data.
    """

    # Get timeline and its events
    timeline = get_object_or_404(Timeline, id=id)
    events = TimelineEvent.objects.filter(timeline__id=id).order_by('-date')

    # Initialize forms
    timeline_details_form = TimelineModelForm(instance=timeline)
    new_event_form = TimelineEventModelForm()
    update_events_formset = EventFormSet(queryset=events)
    formset_helper = EventFormSetHelper()

    # Handle POST request scenarios
    if request.method == 'POST':
        # Timeline details form
        if 'update-timeline-details' in request.POST:
            timeline_details_form = TimelineModelForm(
                request.POST, instance=timeline
            )
            if timeline_details_form.is_valid():
                timeline_details_form.save()
                messages.success(request, 'Timeline details updated!')
                # Re-render form (just and only) in case an empty slug
                # was provided:
                # This would result in an auto-generated slug (see
                # model), in which case the slug field now needs to be
                # repopulated by fetching the object from the database
                timeline_details_form = TimelineModelForm(instance=timeline)
            else:
                # Form was invalid
                messages.error(request, 'Could not update timeline details.')
        # New event form
        elif 'add-event' in request.POST:
            new_event_form = TimelineEventModelForm(request.POST)
            if new_event_form.is_valid():
                event = new_event_form.save(commit=False)
                event.timeline = timeline
                event.save()
                messages.success(request, 'Event saved!')
            else:
                # Form was invalid
                messages.error(request, 'Something went wrong.')
        # Update event(s) form
        else:
            update_events_formset = EventFormSet(request.POST, queryset=events)
            if update_events_formset.is_valid():
                update_events_formset.save()
                messages.success(request, 'Events updated!')
            else:
                # Formset invalid
                messages.error(
                    request, 'Something went wrong updating the event(s).'
                )

    return render(
        request,
        'timelines/edit-timeline.html',
        {
            'timeline': timeline,
            'timeline_details_form': timeline_details_form,
            'new_event_form': new_event_form,
            'update_events_formset': update_events_formset,
            'formset_helper': formset_helper,
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
    messages.info(request, f'Event \'{title}\' deleted.')

    return redirect('timelines:edit', id=timeline_id)


@login_required
def delete_timeline(request, id):
    """
    Takes timeline id as a second argument.
    """
    timeline = get_object_or_404(Timeline, id=id)
    title = timeline.title
    timeline.delete()
    request.session['timeline_count'] = Timeline.objects.filter(
        user=request.user
    ).count()  # Update sidebar menu counter
    messages.info(request, f'Timeline \'{title}\' deleted.')

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
