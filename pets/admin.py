from django.contrib import admin

from pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
