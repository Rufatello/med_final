from django.contrib import admin

from person.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name',)

