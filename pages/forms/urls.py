from django.urls import path
from . import views

urlpatterns = [
    path('general/', views.general, name='forms_general'),
    path('advanced/', views.advanced, name='forms_advanced'),
    path('editors/', views.editors, name='form_editors'),
    path('validation/', views.validation, name='forms_validation'),

]