from django.urls import path
from . import views

urlpatterns = [
    path('pages/invoice/', views.invoice, name='examples_invoice'),
    path('pages/invoice-print/', views.invoice_print, name='examples_invoice-print'),
    path('pages/profile/', views.profile, name='examples_profile'),
    path('pages/e-commerce/', views.e_commerce, name='examples_e-commerce'),
    path('pages/projects/', views.projects, name='examples_projects'),
    path('pages/project-add', views.project_add, name='examples_project-add'),
    path('pages/project-edit', views.project_edit, name='examples_project-edit'),
    path('pages/project-detail', views.project_detail, name='examples_project-detail'),
    path('pages/contacts', views.contacts, name='examples_contacts'),
    path('pages/faq', views.faq, name='examples_faq'),
    path('pages/contact-us', views.contact_us, name='examples_contact-us'),

    path('extras/login-register-v1/login/', views.login, name='examples_login'),
    path('extras/login-register-v1/register/', views.register, name='examples_register'),
    path('extras/login-register-v1/forgot-password/', views.forgot_password, name='examples_forgot-password'),
    path('extras/login-register-v1/recover-password/', views.recover_password, name='examples_recover-password'),

    path('extras/login-register-v2/login-v2/', views.login_v2, name='examples_login-v2'),
    path('extras/login-register-v2/register-v2/', views.register_v2, name='examples_register-v2'),
    path('extras/login-register-v2/forgot-password-v2/', views.forgot_password_v2, name='examples_forgot-password-v2'),
    path('extras/login-register-v2/recover-password-v2/', views.recover_password_v2, name='examples_recover-password-v2'),

    path('extras/lockscreen/', views.lockscreen, name='examples_lockscreen'),
    path('extras/legacy-user-menu/', views.legacy_user_menu, name='examples_legacy-user-menu'),
    path('extras/language-menu/', views.language_menu, name='examples_language-menu'),
    path('extras/404/', views.examples_404, name='examples_404'),
    path('extras/500/', views.examples_500, name='examples_500'),
    path('extras/pace/', views.pace, name='examples_pace'),
    path('extras/blank/', views.blank, name='examples_blank'),
    path('extras/starter/', views.starter, name='examples_starter'),

]