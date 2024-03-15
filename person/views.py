from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from person.models import Person, Product


class PersonViewList(ListView):
    model = Person
    template_name = 'user/base.html'

    def get_queryset(self):
        return Person.objects.all()[:3]


class ProductCreate(CreateView):
    model = Product
    template_name = 'person/product_create.html'
    success_url = reverse_lazy('product:product_list')
    fields = ('name', 'price', 'user', 'descriptions', 'quantity', 'photo')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductList(ListView):
    model = Product
    template_name = 'person/product.html'
    queryset = Product.objects.all()
    context_object_name = 'object_list'
    paginate_by = 3




