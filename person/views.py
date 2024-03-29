import stripe
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormMixin
from person.forms import CommentsForm, AppointmentFormCreate
from person.models import Person, Product, Comments, Specialization, Basket, Appointment


class PersonViewList(ListView):
    """Вывод главной страницы с 3 добавленными врачами"""
    model = Person
    template_name = 'user/base.html'

    def get_queryset(self):
        return Person.objects.all()[:3]


class ProductCreate(CreateView):
    """Добавление пролукта в онлайн аптеку"""
    model = Product
    template_name = 'person/product_create.html'
    success_url = reverse_lazy('person:product')
    fields = ('name', 'price', 'descriptions', 'quantity', 'photo')


class ProductList(ListView):
    """Вывод списка продуктов"""
    model = Product
    template_name = 'person/product.html'
    queryset = Product.objects.all()
    context_object_name = 'object_list'
    paginate_by = 3


class ProductUpdate(UpdateView):
    """Редактирование продукта"""
    model = Product
    template_name = 'person/product_update.html'
    success_url = reverse_lazy('person:product')
    fields = ('name', 'price', 'descriptions', 'photo', 'quantity',)


class ProductDelete(DeleteView):
    """Удаление продукта"""
    model = Product
    template_name = 'person/product_delete.html'
    success_url = reverse_lazy('person:product')


class ProductDetailView(DetailView, FormMixin):
    """подробная информация об 1 продукте в добавлением комментария"""
    model = Product
    template_name = 'person/product_view.html'
    form_class = CommentsForm
    success_url = reverse_lazy('person:product')

    # def get_success_url(self):
    #     return reverse_lazy('product_view', kwargs={'pk': self.get_object().id})

    def post(self, requests, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.product = self.get_object()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class CommendDelete(DeleteView):
    """Удаление владельцем комментария"""
    model = Comments
    template_name = 'person/comments_delete.html'
    success_url = reverse_lazy('person:product')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user and not self.request.user.is_staff:
            raise Http404("Вы не являетесь владельцем этого клиента")
        return self.object


class PersonView(ListView):
    """Вывод списка врачей с пагинацией"""
    model = Person
    template_name = 'person/person_list.html'
    context_object_name = 'object_list'
    paginate_by = 3


class PersonDetailView(DetailView, FormMixin):
    """Подробная информация о враче с добавлением комментария"""
    model = Person
    template_name = 'person/person_view.html'
    form_class = CommentsForm
    success_url = reverse_lazy('person:person_list')

    # def get_success_url(self):
    #     return reverse('person_view', kwargs={'pk': self.object.pk})

    def post(self, requests, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.person = self.get_object()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class CommendPersonDelete(DeleteView):
    """Удаление владельцем комментария у врача"""
    model = Comments
    template_name = 'person/person_coments_delete.html'
    success_url = reverse_lazy('person:person_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user and not self.request.user.is_staff:
            raise Http404("Вы не являетесь владельцем этого клиента")
        return self.object


class SpecializationCreate(CreateView):
    """Добавление специализации"""
    model = Specialization
    template_name = 'person/specialization_create.html'
    success_url = reverse_lazy('person:specialization')
    fields = '__all__'


class SpecializationList(ListView):
    """Вывод списка специализаций с пагинацией"""
    model = Specialization
    template_name = "person/specialization.html"
    paginate_by = 3


class SpecializationUpdate(UpdateView):
    """Редактирование специализации"""
    model = Specialization
    template_name = 'person/product_update.html'
    success_url = reverse_lazy('person:specialization')
    fields = ('name', 'descriptions', 'photo',)


class SpecializationDelete(DeleteView):
    """Удаление специализации"""
    model = Specialization
    template_name = 'person/specialization_delete.html'
    success_url = reverse_lazy('person:specialization')


class PersonUpdate(UpdateView):
    """Редактирование врача"""
    model = Person
    template_name = 'person/person_update.html'
    success_url = reverse_lazy('person:person_list')
    fields = '__all__'


class PersonListView(ListView):
    """Вывод списка врачей согластно категории"""
    model = Product
    template_name = 'person/person.html'
    context_object_name = 'object_list'
    paginate_by = 3

    def get_queryset(self):
        specialization_id = self.kwargs['category_id']
        specialization = Specialization.objects.get(id=specialization_id)
        return Person.objects.filter(specialization=specialization)


class PersonCreate(CreateView):
    """Добавление врача"""
    model = Person
    template_name = 'person/person_create.html'
    fields = '__all__'
    success_url = reverse_lazy('person:person_list')


class PersonDelete(DeleteView):
    """Удаление врача"""
    model = Person
    template_name = 'person/person_delete.html'
    success_url = reverse_lazy('person:person_list')


class ContactView(View):
    """Вывод страницы с обратной связью"""
    template_name = 'person/contact.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(name, phone, message)
        return render(request, self.template_name)


def basket_add(request, pk):
    """сделано добавление товаров в корзину,
    количество продуктов в корзине увеличивается на 1 и запись в корзине сохраняется"""
    product = Product.objects.get(pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product)

    if not basket.exists():
        Basket.objects.create(
            user=request.user,
            product=product,
            quantity=1
        )
    else:
        basket = basket.first()
        basket.quantity+=1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    """удаление продукта с корзины"""
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class AppointmentCreate(CreateView):
    """добавление записи к врачу"""
    model = Appointment
    template_name = 'person/appointment_create.html'
    success_url = reverse_lazy('user:profile')
    form_class = AppointmentFormCreate

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class AppointmentUpdate(UpdateView):
    """Редактирование записи к врачу"""
    model = Appointment
    fields = ('person', 'data', 'time',)
    template_name = 'person/appointment_update.html'
    success_url = reverse_lazy('user:profile')


class AppointmentDelete(DeleteView):
    """Удаление записи к врачу"""
    model = Appointment
    template_name = 'person/appointment_delete.html'
    success_url = reverse_lazy('user:profile')


def payments_create(request):
    """создание суммы и платежной ссылки"""
    stripe.api_key = 'sk_test_51OdoXSHC8LUh8NqZQboynIwfP7znL7qfNqCOqOYkl7k3pzAKN8QU45ye5RpnABJ2MRjLBfk6tWWisTmY9QoiXJNR00NP3ImbNV'
    baskets = Basket.objects.filter(user=request.user)
    total_sum = sum(basket.sum() for basket in baskets)
    payments_create = stripe.Price.create(
        currency="usd",
        unit_amount=int(total_sum)*100,
        recurring={"interval": "month"},
        product_data={"name": 'dsadas'},
    )
    payment_intent = stripe.PaymentLink.create(
        line_items=[{"price": payments_create.id, "quantity": 1}])

    if request.method == 'GET':
        return payment_intent.url


def perehod(request):
    """Добавление ссылки"""
    payment_url = payments_create(request)
    return redirect(payment_url)

