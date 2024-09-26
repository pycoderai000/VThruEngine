from django.urls import path
from . import views

urlpatterns = [
    # Cart Apis
    path('cart', views.CartView.as_view()), # Get and Post Apis
    path('update/cart/<int:pk>/', views.CartUpdateView.as_view()), # Update and Delete Apis

    # Category Apis
    path('category', views.CategoryView.as_view()), # Get and Post Apis
    path('update/category/<int:pk>/', views.CategoryUpdateView.as_view()), # Update and Delete Apis
]
