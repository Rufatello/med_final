from django.forms import forms
from person.models import Person


class PersonForm(forms.Form):
    model = Person
    fields = '__all__'

