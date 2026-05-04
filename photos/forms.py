from django.forms import ModelForm
from django import forms
from photos.models import Photo


class PhotoBaseForm(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

        widgets = {
            'photo': forms.FileInput(attrs={'placeholder': 'Upload photo'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'rows': 3}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'tagged_pets': forms.SelectMultiple(attrs={'placeholder': 'Tag pets'}),
        }

        labels = {
            'photo': 'Photo',
            'description': 'Description',
            'location': 'Location',
            'tagged_pets': 'Tagged Pets',
        }

class PhotoCreateForm(PhotoBaseForm):
    ...


class PhotoEditForm(PhotoBaseForm):
    ...


class PhotoDeleteForm(PhotoBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True