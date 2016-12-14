from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^form/', views.get_name, name='form'),

]