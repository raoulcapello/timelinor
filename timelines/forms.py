from django import forms
from crispy_forms.helper import FormHelper

from .models import Timeline, TimelineEvent


class TimelineModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'form-label'

    class Meta:
        model = Timeline
        fields = [
            'title',
            'description',
        ]

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'i.e. \'Job History\' or \'Education\''}
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Max. 200 characters looks best on the timeline.',
                'rows': 5,
            }
        )
    )
