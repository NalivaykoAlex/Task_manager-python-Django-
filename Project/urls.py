from django.conf.urls import url
from Project import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create$', views.CreateTaskView.as_view(), name='create'),
    url(r'^delete(?P<pk>\d+)/$', views.DeleteTaskView.as_view(), name='delete'),
    url(r'^detail(?P<pk>\d+)/$', views.DetailTaskView.as_view(), name='detail'),
    url(r'^update(?P<pk>\d+)/$', views.UpdateTaskView.as_view(), name='update'),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^author_task/$', views.AuthorTaskView.as_view(), name='author_task'),
    url(r'^to_author_task/$', views.ToAuthorTaskView.as_view(), name='to_author_task'),

]
