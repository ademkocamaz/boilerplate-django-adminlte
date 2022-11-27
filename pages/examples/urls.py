from django.urls import path
from . import views

urlpatterns = [
    path('invoice/', views.invoice, name='examples_invoice'),
    path('invoice-print/', views.invoice_print, name='examples_invoice-print'),
    path('profile/', views.profile, name='examples_profile'),
    path('e-commerce/', views.e_commerce, name='examples_e-commerce'),
    path('projects/', views.projects, name='examples_projects'),
    path('project-add', views.project_add, name='examples_project-add'),
    path('project-edit', views.project_edit, name='examples_project-edit'),
    path('project-detail', views.project_detail, name='examples_project-detail'),
    path('contacts', views.contacts, name='examples_contacts'),
    path('faq', views.faq, name='examples_faq'),
    path('contact-us', views.contact_us, name='examples_contact-us'),

]