from django.contrib.admin.widgets import AdminDateWidget
from django.forms import Textarea
from django import forms
from person.models import Comments, Appointment


class CommentsForm(forms.ModelForm):
    """Форма для добавления комментария"""
    class Meta:
        model = Comments
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget = Textarea(attrs={'rows': 5})


class AppointmentFormCreate(forms.ModelForm):
    """Форма для записи к врачу"""
    data = forms.DateField(widget=AdminDateWidget)

    class Meta:
        model = Appointment
        fields = ('person', 'data', 'time',)
