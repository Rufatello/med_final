from django.conf import settings
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView as BaseLoginView, PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, UpdateView

from person.models import Basket
from users.forms import UserForm, UserFormUpdate, PasswordChangingForm
from users.models import User
from users.services import generation, new_pass


class ProfileView(View):
    template_name = 'user/profile.html'

    def get(self, request):
        baskets = Basket.objects.filter(user=request.user)
        total_sum = sum(basket.sum() for basket in baskets)
        total_quantity = sum(basket.quantity for basket in baskets)

        context = {
            'total_sum': total_sum,
            'baskets': baskets,
            'total_quantity': total_quantity

        }
        return render(request, self.template_name, context)


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
            return redirect('person:home')


class LoginView(BaseLoginView):
    template_name = 'user/login.html'


def LogoutUser(request):
    logout(request)

    return redirect('person:home')


class UserUpdate(UpdateView):
    model = User
    form_class = UserFormUpdate
    template_name = 'user/update.html'
    success_url = reverse_lazy('person:home')

    def get_object(self, queryset=None):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('user:login')
    template_name = 'user/user_password.html'


def new_password(request):
    a = new_pass(request)
    return a