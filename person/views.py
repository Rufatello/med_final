from django.views.generic import ListView
from person.models import Person


class PersonViewList(ListView):
    model = Person
    template_name = 'user/base.html'

    def get_queryset(self):
        return Person.objects.all()[:3]




