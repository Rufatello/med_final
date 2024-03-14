from django.urls import path
from users.apps import UsersConfig
from . import views
from .views import LoginView

app_name = UsersConfig.name


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('reg/', views.Registrations.as_view(), name='register'),
    path('code/', views.CodeView.as_view(), name='code'),
    path('logout/', views.LogoutUser, name='logout'),
    path('login/', LoginView.as_view(), name='login'),
]