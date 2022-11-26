from django.urls import path
from . import views

urlpatterns = [
    path('top-nav/', views.top_nav, name='layout_top-nav'),
    path('top-nav-sidebar/', views.top_nav_sidebar, name='layout_top-nav-sidebar'),
    path('boxed/', views.boxed, name='layout_boxed'),
    path('fixed-sidebar/', views.fixed_sidebar, name='layout_fixed-sidebar'),
    path('fixed-sidebar-custom/', views.fixed_sidebar_custom, name='layout_fixed-sidebar-custom'),
    path('fixed-topnav/', views.fixed_topnav, name='layout_fixed-topnav'),
    path('fixed-footer/', views.fixed_footer, name='layout_fixed-footer'),
    path('collapsed-sidebar/', views.collapsed_sidebar, name='layout_collapsed-sidebar'),
    



]
