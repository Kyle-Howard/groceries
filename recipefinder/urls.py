from django.urls import path
from recipefinder import views as views

urlpatterns = [
    path('home', views.home),
    path('search_recipes', views.search_recipes),
    path('update_cart', views.update_cart),
    path('remove_from_cart', views.remove_from_cart),
    path('create_list', views.create_list)
]