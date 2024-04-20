from admin_datta.forms import LoginForm, RegistrationForm
from django import forms
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
# from django.forms.widgets import BootstrapDateTimePickerInput
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

# from manager.forms import TaskCreationForm
from manager.models import Task, Worker


@login_required
def index(request):
    count_tasks = Task.objects.count()
    count_workers = Worker.objects.count()
    workers = Worker.objects.all()
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        'workers': workers,
        'count_tasks': count_tasks,
        'count_workers': count_workers,
    }
    return render(request, "manager/index.html", context=context)


def tables(request):
    context = {
        'segment': 'tables'
    }
    return render(request, "pages/components/dynamic-tables.html", context)


class WorkerListView(generic.ListView):
    model = Worker
    paginate_by = 5
    queryset = Worker.objects.all()


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks_list"
    template_name = "manager/task_list.html"
    paginate_by = 5


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    # form_class = TaskCreationForm
    fields = ["name", "description", "deadline", "priority", "task_type", "assignees",]
    # deadline = forms.DateTimeField(input_formats=["%Y/%m/%d %H:%M"], widget=BootstrapDateTimePickerInput())


def add_remove_from_task(request, pk):
    worker = Worker.objects.get(id=request.user.id)
    if Task.objects.get(id=pk) in worker.assignees.all():
        worker.assignees.remove(pk)
    else:
        worker.assignees.add(pk)
    return HttpResponseRedirect(reverse_lazy("manager:task-detail", args=[pk]))


class UserRegistrationView(CreateView):
  template_name = 'accounts/auth-signup.html'
  form_class = RegistrationForm
  success_url = '/accounts/login/'


class UserLoginView(LoginView):
  template_name = 'accounts/auth-signin.html'
  form_class = LoginForm


def logout_view(request):
  logout(request)
  return redirect('/accounts/login/')
