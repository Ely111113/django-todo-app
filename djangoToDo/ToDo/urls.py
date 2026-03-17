from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("edit/<int:task_id>/", views.edit, name="edit"),
    path("delete/<int:task_id>/", views.delete, name="delete"),
    path("done/<int:task_id>/", views.done, name="done"),
    path("", views.index, name="index"), 
]