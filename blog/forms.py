from django import forms
from .models import comment


class post_comment(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['content']
        labels = {
            'comment'
        }