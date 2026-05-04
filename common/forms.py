from django import forms
from django.forms import Form
from django.forms.models import ModelForm

from common.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Add comment...'})
        }



class SearchForm(forms.Form):
    pet_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Search by pet name...'}))

