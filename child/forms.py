from django import forms
from .models import submission

class submission_form(forms.ModelForm):
    class Meta:
        model = submission
        fields = ['title', 'description', 'images']
