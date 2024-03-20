from django.urls import path
from person.apps import PersonConfig
from . import views
from .views import ContactView

app_name = PersonConfig.name


urlpatterns = [
    path('', views.PersonViewList.as_view(), name='home'),
    path('product/', views.ProductList.as_view(), name='product'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),
    path('product/create/', views.ProductCreate.as_view(), name='product_create'),
    path('product/<int:pk>/view/', views.ProductDetailView.as_view(), name='product_view'),
    path('comment/<int:pk>/delete/', views.CommendDelete.as_view(), name='comment_delete'),
    path('person_list/', views.PersonView.as_view(), name='person_list'),
    path('person/<int:pk>/view', views.PersonDetailView.as_view(), name='person_view'),
    path('comment_person/<int:pk>/delete/', views.CommendPersonDelete.as_view(), name='comment_delete_person'),
    path('specialization/', views.SpecializationList.as_view(), name='specialization'),
    path('comment_person/create/', views.SpecializationCreate.as_view(), name='specialization_create'),
    path('specilization_update/<int:pk>/', views.SpecializationUpdate.as_view(), name='specialization_update'),
    path('specilization_delete/<int:pk>/', views.SpecializationDelete.as_view(), name='specialization_delete'),
    path('person_update/<int:pk>/', views.PersonUpdate.as_view(), name='person_update'),
    path('person/<int:category_id>/', views.PersonListView.as_view(), name='person_person'),
    path('person_create/', views.PersonCreate.as_view(), name='person_create'),
    path('person/<int:pk>/delete/', views.PersonDelete.as_view(), name='person_delete'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('basket_add/<int:pk>/', views.basket_add, name='basket_add'),
    path('basket_remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
    path('appointment_create/', views.AppointmentCreate.as_view(), name='appointment_create'),
    path('appointment_update/<int:pk>/', views.AppointmentUpdate.as_view(), name='appointment_update'),
    path('appointment_delete/<int:pk>/', views.AppointmentDelete.as_view(), name='appointment_delete'),

]