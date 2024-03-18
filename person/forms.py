from django.forms import forms, Textarea
from django import forms
from person.models import Person, Comments


class PersonForm(forms.Form):
    model = Person
    fields = '__all__'


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget = Textarea(attrs={'rows': 5})

