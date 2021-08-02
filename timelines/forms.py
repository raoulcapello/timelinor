from django import forms
from django.forms import modelformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML, Div

from .models import Timeline, TimelineEvent


# Formset (and Helper) to allow updating of one or more events of a
# single timeline at once
EventFormSet = modelformset_factory(
    TimelineEvent,
    fields=('date', 'title', 'subtitle', 'description'),
    labels={
        'date': (
            'Note that the date you select here is only used to \
                chronologically order your timeline, but will not be shown on \
                    timeline. This field is required.'
        )
    },
    widgets={
        'date': forms.DateInput(
            attrs={
                'placeholder': 'Choose a date (required)',
                'class': 'date-picker rounded pe-5',
            }
        ),
        'title': forms.TextInput(
            attrs={'placeholder': 'i.e. \'2021\' or \'May 2021\''}
        ),
        'subtitle': forms.TextInput(
            attrs={'placeholder': 'i.e. \'Web Developer\' or \'Designer\''}
        ),
        'description': forms.Textarea(
            attrs={
                'placeholder': (
                    'Max. 200 characters looks best on the timeline.'
                ),
                'rows': 5,
            }
        ),
    },
    extra=0,
)


class EventFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_class = 'form-label'
        self.form_tag = False


class TimelineModelForm(forms.ModelForm):
    class Meta:
        model = Timeline
        fields = [
            'title',
            'description',
            'slug',
            'button',
            'button_text',
            'button_url',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'form-label'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'title',
                'description',
                'slug',
                Div(
                    HTML(
                        (
                            'The \'slug\' is used to provide you with a custom \
                            public URL to your timeline graph, so you can \
                            share it with the world. If you don\'t provide \
                            one, it will be automatically generated.'
                        ),
                    ),
                    css_class='form-text',
                ),
            ),
            Fieldset(
                '<hr class="my-5">(Optional) Custom Homepage Button Settings',
                Div(
                    'button',
                    css_class='form-check form-switch',
                ),
                Div(
                    HTML(
                        (
                            'Activates an optional button on the public \
                            timeline page. This allows you to redirect \
                            your users back to  your own domain.'
                        ),
                    ),
                    css_class='form-text mb-3',
                ),
                'button_text',
                'button_url',
            ),
        )

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'i.e. \'Job History\' or \'Education\''}
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': (
                    'Max. 200 characters looks best on the timeline.'
                ),
                'rows': 5,
            }
        )
    )
    slug = forms.SlugField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'i.e. \'my-first-slug\'',
            }
        ),
    )
    button = forms.BooleanField(
        required=False,
        label=('Show button on public page'),
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
            }
        ),
    )
    button_text = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'i.e. Back to my homepage'}
        ),
    )
    button_url = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={'placeholder': 'i.e. www.your-domain.com'}
        ),
    )


class TimelineEventModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'form-label'

    class Meta:
        model = TimelineEvent
        fields = [
            'date',
            'title',
            'subtitle',
            'description',
        ]

    date = forms.DateField(
        label=(
            'Note that the date you select here is only used to \
                chronologically order your timeline, but will not be shown on \
                    timeline. This field is required.'
        ),
        widget=forms.DateInput(
            attrs={
                'placeholder': 'Choose a date (required)',
                'class': 'date-picker rounded pe-5',
            }
        ),
    )
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'i.e. \'2021\' or \'May 2021\''}
        )
    )
    subtitle = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'i.e. \'Web Developer\' or \'Designer\''}
        ),
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': (
                    'Max. 200 characters looks best on the timeline.'
                ),
                'rows': 5,
            }
        ),
    )
