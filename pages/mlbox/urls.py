from django.urls import path
from . import views

urlpatterns = [
    path('mailbox/', views.mailbox, name='mailbox_mailbox'),
    path('compose/', views.compose, name='mailbox_compose'),
    path('read-mail/', views.read_mail, name='mailbox_read-mail'),

]