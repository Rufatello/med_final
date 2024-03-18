from django.urls import path
from person.apps import PersonConfig
from . import views


app_name = PersonConfig.name


urlpatterns = [
    path('', views.PersonViewList.as_view(), name='home'),
    path('product/', views.ProductList.as_view(), name='product'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),
    path('product/create/', views.ProductCreate.as_view(), name='product_create'),
    path('product/<int:pk>/view/', views.ProductDetailView.as_view(), name='product_view'),

]