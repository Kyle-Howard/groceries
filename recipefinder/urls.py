from django.urls import path
from recipefinder import views as views

urlpatterns = [
    path('search_recipes', views.search_recipes),
    path('update_cart', views.update_cart)
]