from django.forms import ModelForm
from django import forms

from pets.models import Pet


class PetBaseForm(ModelForm):
    class Meta:
        model = Pet
        exclude = ['slug']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'personal_photo': forms.TextInput(attrs={'placeholder': 'Link to image'}),
        }

        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of Birth',
            'personal_photo': "Link to Image",
        }


class PetCreateForm(PetBaseForm):
    ...


class PetEditForm(PetBaseForm):
    ...


class PetDeleteForm(PetBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
