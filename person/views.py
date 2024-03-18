from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormMixin

from person.forms import CommentsForm
from person.models import Person, Product, Comments


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





