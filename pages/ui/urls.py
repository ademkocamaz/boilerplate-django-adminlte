from django.urls import path
from . import views

urlpatterns = [
    path('general/', views.general, name='general'),
    path('icons/', views.icons, name='icons'),
    path('buttons/', views.buttons, name='buttons'),
    path('sliders/', views.sliders, name='sliders'),
    path('modals/', views.modals, name='modals'),
    path('navbar/', views.navbar, name='navbar'),
    path('timeline/', views.timeline, name='timeline'),
    path('ribbons/', views.ribbons, name='ribbons'),

]