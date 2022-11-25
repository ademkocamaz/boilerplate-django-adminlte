from django.urls import path
from . import views

urlpatterns = [
    path('top-nav/', views.top_nav, name='top-nav'),
    path('top-nav-sidebar/', views.top_nav_sidebar, name='top-nav-sidebar'),
    path('boxed/', views.boxed, name='boxed'),
    path('fixed-sidebar/', views.fixed_sidebar, name='fixed-sidebar'),
    path('fixed-sidebar-custom/', views.fixed_sidebar_custom, name='fixed-sidebar-custom'),
    path('fixed-topnav/', views.fixed_topnav, name='fixed-topnav'),
    path('fixed-footer/', views.fixed_footer, name='fixed-footer'),
    path('collapsed-sidebar/', views.collapsed_sidebar, name='collapsed-sidebar'),
    



]
