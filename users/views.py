from django.conf import settings
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView as BaseLoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from users.forms import UserForm
from users.models import User
from users.services import generation


# class HomeView(View):
#     template_name = 'user/base.html'
#
#     def get(self, request):
#         return render(request, self.template_name)
#

class Registrations(CreateView):
    template_name = 'user/register.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('user:code')

    def form_valid(self, form):
        password = generation()
        new_user = form.save(commit=False)
        new_user.code = password
        new_user.save()
        send_mail(
            subject='Подтверждение регистрации',
            message=f' Введите код: {new_user.code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )

        return super().form_valid(form)


class CodeView(View):
    model = User
    template_name = 'user/code.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        code = request.POST.get('code')
        user = User.objects.filter(code=code).first()

        if user is not None and user.code == code:
            user.is_active = True
            user.save()
            return redirect('users:home')


class LoginView(BaseLoginView):
    template_name = 'user/login.html'


def LogoutUser(request):
    logout(request)

    return redirect('person:home')