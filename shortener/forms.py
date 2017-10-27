from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

from .validators import validate_url

class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='Submit Form', validators=[validate_url])
