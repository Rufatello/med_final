from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormMixin
from person.forms import CommentsForm
from person.models import Person, Product, Comments, Specialization, Basket


class PersonViewList(ListView):
    model = Person
    template_name = 'user/base.html'

    def get_queryset(self):
        return Person.objects.all()[:3]


class ProductCreate(CreateView):
    model = Product
    template_name = 'person/product_create.html'
    success_url = reverse_lazy('person:product')
    fields = ('name', 'price', 'descriptions', 'quantity', 'photo')


class ProductList(ListView):
    model = Product
    template_name = 'person/product.html'
    queryset = Product.objects.all()
    context_object_name = 'object_list'
    paginate_by = 3


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'person/product_update.html'
    success_url = reverse_lazy('person:product')
    fields = ('name', 'price', 'descriptions', 'photo', 'quantity',)


class ProductDelete(DeleteView):
    model = Product
    template_name = 'person/product_delete.html'
    success_url = reverse_lazy('person:product')


class ProductDetailView(DetailView, FormMixin):
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
    model = Comments
    template_name = 'person/comments_delete.html'
    success_url = reverse_lazy('person:product')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user and not self.request.user.is_staff:
            raise Http404("Вы не являетесь владельцем этого клиента")
        return self.object


class PersonView(ListView):
    model = Person
    template_name = 'person/person_list.html'
    context_object_name = 'object_list'
    paginate_by = 3


class PersonDetailView(DetailView, FormMixin):
    model = Person
    template_name = 'person/person_view.html'
    form_class = CommentsForm
    success_url = reverse_lazy('person:person_list')

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
        self.object.person = self.get_object()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class CommendPersonDelete(DeleteView):
    model = Comments
    template_name = 'person/person_coments_delete.html'
    success_url = reverse_lazy('person:person_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user and not self.request.user.is_staff:
            raise Http404("Вы не являетесь владельцем этого клиента")
        return self.object


class SpecializationCreate(CreateView):
    model = Specialization
    template_name = 'person/specialization_create.html'
    success_url = reverse_lazy('person:specialization')
    fields = '__all__'


class SpecializationList(ListView):
    model = Specialization
    template_name = "person/specialization.html"
    paginate_by = 3


class SpecializationUpdate(UpdateView):
    model = Product
    template_name = 'person/product_update.html'
    success_url = reverse_lazy('person:specialization')
    fields = ('name', 'price', 'descriptions', 'photo', 'quantity',)


class SpecializationDelete(DeleteView):
    model = Specialization
    template_name = 'person/specialization_delete.html'
    success_url = reverse_lazy('person:specialization')


class PersonUpdate(UpdateView):
    model = Person
    template_name = 'person/person_update.html'
    success_url = reverse_lazy('person:person_list')
    fields = '__all__'


class PersonListView(ListView):
    model = Product
    template_name = 'person/person.html'
    context_object_name = 'object_list'
    paginate_by = 3

    def get_queryset(self):
        specialization_id = self.kwargs['category_id']
        specialization = Specialization.objects.get(id=specialization_id)
        return Person.objects.filter(specialization=specialization)


class PersonCreate(CreateView):
    model = Person
    template_name = 'person/person_create.html'
    fields = '__all__'
    success_url = reverse_lazy('person:person_list')


class PersonDelete(DeleteView):
    model = Person
    template_name = 'person/person_delete.html'
    success_url = reverse_lazy('person:person_list')


class ContactView(View):
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