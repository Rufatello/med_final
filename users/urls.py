from django.urls import path
from users.apps import UsersConfig
from . import views
from .views import LoginView, new_password, PasswordsChangeView

app_name = UsersConfig.name


urlpatterns = [
    path('reg/', views.Registrations.as_view(), name='register'),
    path('code/', views.CodeView.as_view(), name='code'),
    path('logout/', views.LogoutUser, name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('update/', views.UserUpdate.as_view(), name='update'),
    path('newpassword/', new_password, name='new_password'),
    path('user_password/', PasswordsChangeView.as_view(), name='user_password'),

]