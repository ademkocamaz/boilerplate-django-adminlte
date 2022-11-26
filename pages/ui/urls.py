from django.urls import path
from . import views

urlpatterns = [
    path('general/', views.general, name='ui_general'),
    path('icons/', views.icons, name='ui_icons'),
    path('buttons/', views.buttons, name='ui_buttons'),
    path('sliders/', views.sliders, name='ui_sliders'),
    path('modals/', views.modals, name='ui_modals'),
    path('navbar/', views.navbar, name='ui_navbar'),
    path('timeline/', views.timeline, name='ui_timeline'),
    path('ribbons/', views.ribbons, name='ui_ribbons'),

]