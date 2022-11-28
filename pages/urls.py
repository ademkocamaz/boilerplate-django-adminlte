from django.urls import path, include
from . import views

urlpatterns = [
    path('widgets/', views.widgets, name='widgets'),
    path('layout/', include('pages.layout.urls')),
    path('charts/', include('pages.charts.urls')),
    path('ui/', include('pages.ui.urls')),
    path('forms/', include('pages.forms.urls')),
    path('tables/', include('pages.tables.urls')),
    path('calendar/', views.calendar, name='calendar'),
    path('gallery/', views.gallery, name='gallery'),
    path('kanban/', views.kanban, name='kanban'),
    path('mailbox/', include('pages.mlbox.urls')),
    path('examples/', include('pages.examples.urls')),
    path('search/', include('pages.search.urls')),

]
