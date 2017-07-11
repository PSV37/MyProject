from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$',views.IndexView.as_view(), name='index'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view() , name='detail'),

    url(r'^register/$',views.UserFormView.as_view(), name="register" ),

    url(r'^login/$',views.UserLoginForm.as_view(), name="login" ),

    url(r'^movie/add/$',views.MovieAdd.as_view(), name="movie_add"),

    url(r'^edit/(?P<pk>[0-9]+)/$',views.MovieUpdate.as_view(), name="movie-up"),

    url(r'^app/(?P<pk>[0-9]+)/delete/$',views.MovieDelete.as_view(), name="movie-del"),
]