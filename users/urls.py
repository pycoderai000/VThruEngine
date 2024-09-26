from django.urls import path
from . import views

urlpatterns = [
    path('', views.User.as_view()),
    path("password/reset/", views.user_password_reset_request.as_view()),

]
