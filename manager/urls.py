from django.urls import path

from manager import views
from manager.views import index, tables, TaskListView, TaskDetailView, add_remove_from_task, TaskCreateView

urlpatterns = [
    path("", index, name="index"),
    path("tables/", tables, name="tables"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/add_remove", add_remove_from_task, name="add-remove-from-task"),
    path('accounts/register/', views.UserRegistrationView.as_view(), name="register"),
    path('accounts/login/', views.UserLoginView.as_view(), name="login"),
    path('accounts/logout/', views.logout_view, name="logout"),
]


app_name = "manager"
