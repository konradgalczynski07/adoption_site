from django.contrib import admin

from .models import Pet

class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published', 'list_date', 'volunteer')
    list_display_links = ('id', 'name')
    list_filter = ('volunteer',)
    list_editable = ('is_published',)
    search_fields = ('name', 'description', 'city', 'race', 'gender', 'age')
    list_per_page = 25


admin.site.register(Pet, PetAdmin)