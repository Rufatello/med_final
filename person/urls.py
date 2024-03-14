from django.urls import path
from person.apps import PersonConfig
from . import views


app_name = PersonConfig.name


urlpatterns = [
    path('', views.PersonViewList.as_view(), name='home'),

]