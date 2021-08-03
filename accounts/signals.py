from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from timelines.models import Timeline, TimelineEvent

import datetime

User = get_user_model()


def my_first_timeline(sender, instance, created, **kwargs):
    """
    Create a first, demo timeline for new users.
    """
    if created:
        # Create a timeline object
        timeline = Timeline.objects.create(
            user=instance,
            title='My First Timeline',
            description=(
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
            ),
        )
        # Create several events and place them on the newly created
        # timeline
        TimelineEvent.objects.create(
            timeline=timeline,
            title='2021',
            subtitle='Web Developer',
            description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum mattis felis vitae risus pulvinar tincidunt. Nam ac venenatis enim. Aenean hendrerit justo sed. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum mattis felis vitae risus pulvinar tincidunt. Nam ac venenatis enim. Aenean hendrerit justo sed. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum mattis felis vitae risus pulvinar tincidunt. Nam ac venenatis enim. Aenean hendrerit justo sed.',
            date=datetime.date(2021, 8, 1),
        )
        TimelineEvent.objects.create(
            timeline=timeline,
            title='2020',
            subtitle='Web Designer',
            description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum mattis felis vitae risus pulvinar tincidunt. Nam ac venenatis enim. Aenean hendrerit justo sed. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum mattis felis vitae risus pulvinar tincidunt. Nam ac venenatis enim. Aenean hendrerit justo sed. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum mattis felis vitae risus pulvinar tincidunt. Nam ac venenatis enim. Aenean hendrerit justo sed.',
            date=datetime.date(2020, 8, 1),
        )
        TimelineEvent.objects.create(
            timeline=timeline,
            title='2019',
            subtitle='DevOps Engineer',
            description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum mattis felis vitae risus pulvinar tincidunt. Nam ac venenatis enim. Aenean hendrerit justo sed. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum mattis felis vitae risus pulvinar tincidunt. Nam ac venenatis enim. Aenean hendrerit justo sed. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum mattis felis vitae risus pulvinar tincidunt. Nam ac venenatis enim. Aenean hendrerit justo sed.',
            date=datetime.date(2019, 8, 1),
        )
        TimelineEvent.objects.create(
            timeline=timeline,
            title='2018',
            subtitle='Systems Engineer',
            description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum mattis felis vitae risus pulvinar tincidunt. Nam ac venenatis enim. Aenean hendrerit justo sed. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum mattis felis vitae risus pulvinar tincidunt. Nam ac venenatis enim. Aenean hendrerit justo sed. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum mattis felis vitae risus pulvinar tincidunt. Nam ac venenatis enim. Aenean hendrerit justo sed.',
            date=datetime.date(2018, 8, 1),
        )
        TimelineEvent.objects.create(
            timeline=timeline,
            title='2017',
            subtitle='Network Engineer',
            description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum mattis felis vitae risus pulvinar tincidunt. Nam ac venenatis enim. Aenean hendrerit justo sed. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum mattis felis vitae risus pulvinar tincidunt. Nam ac venenatis enim. Aenean hendrerit justo sed. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum mattis felis vitae risus pulvinar tincidunt. Nam ac venenatis enim. Aenean hendrerit justo sed.',
            date=datetime.date(2017, 8, 1),
        )


post_save.connect(my_first_timeline, sender=User)
