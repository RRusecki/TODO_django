from django.urls import path
from . import views
from .views import register, login_view

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("create/", views.create_task, name="create_task"),
    path("edit/<int:task_id>/", views.edit_task, name="edit_task"),
    path("delete/<int:task_id>", views.delete_task, name="delete_task"),
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]