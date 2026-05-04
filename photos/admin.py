from django.contrib import admin

from photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_of_publication', 'description', 'tagged_pets']

    @staticmethod
    def tagged_pets(obj):
        return ', '.join([p.name for p in obj.tagged_pets.all()])

