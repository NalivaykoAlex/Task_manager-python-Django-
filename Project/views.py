# -*- coding: utf-8 -*-
from datetime import datetime
from django.http.response import Http404
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.views import generic
from Project.models import Task


class IndexView(generic.ListView):
    model = Task
    template_name = 'Tasks/template/main.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super(IndexView, self).get_queryset(*args, **kwargs)
        return queryset.filter()

    def get_context_data(self, **kwargs):
        context_data = super(IndexView, self).get_context_data(**kwargs)
        a = {'name_table': 'Все задачи:'}
        context_data.update(a)
        return context_data


class AuthorTaskView(generic.ListView):
    model = Task
    template_name = 'Tasks/template/main.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super(AuthorTaskView, self).get_queryset(*args, **kwargs)
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context_data = super(AuthorTaskView, self).get_context_data(**kwargs)
        a = {'name_table': 'Список задач созданных пользователем:'}
        context_data.update(a)
        return context_data


class ToAuthorTaskView(generic.ListView):
    model = Task
    template_name = 'Tasks/template/main.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super(ToAuthorTaskView, self).get_queryset(*args, **kwargs)
        return queryset.filter(assigned_to_user=self.request.user)

    def get_context_data(self, **kwargs):
        context_data = super(ToAuthorTaskView, self).get_context_data(**kwargs)
        a = {'name_table': 'Список задач для пользователя:'}
        context_data.update(a)
        return context_data


class CreateTaskView(generic.CreateView):
    model = Task
    template_name = 'Tasks/create.html'
    fields = ['name', 'detail', 'assigned_to_user']

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTaskView, self).form_valid(form)


class DeleteTaskView(generic.DeleteView):
    model = Task
    template_name = 'Tasks/delete.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise Http404('Не достаточно прав для удаления')
        return super(DeleteTaskView, self).dispatch(request, *args, **kwargs)


class DetailTaskView(generic.DetailView):
    model = Task
    template_name = 'Tasks/detail.html'


class UpdateTaskView(generic.UpdateView):
    model = Task
    template_name = 'Tasks/update.html'
    success_url = '/'
    fields = ['name', 'detail', 'assigned_to_user', 'completed']

    def dispatch(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs.get('pk'))
        if not self.request.user.is_superuser and (task.completed or task.user != self.request.user):
            raise Http404('Не достаточно прав для редактирования')
        return super(UpdateTaskView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if form.instance.completed:
           if not form.instance.date_off:
               form.instance.date_off= datetime.now()
        else:
            form.instance.date_off = None
        return super(UpdateTaskView, self).form_valid(form)


class RegisterFormView(FormView):
    form_class = UserCreationForm
    template_name = 'Tasks/register.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'Tasks/login.html'
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
