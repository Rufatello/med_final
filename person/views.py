from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from person.models import Person, Product


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








