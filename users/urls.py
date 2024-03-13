from django.urls import path
from users.apps import UsersConfig
from . import views
app_name = UsersConfig.name


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]