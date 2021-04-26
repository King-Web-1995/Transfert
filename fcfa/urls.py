from django.urls import path
from . import views


urlpatterns = [
	path('index', views.index, name='index'),
    path('depense', views.depense, name='depense'),
    path('', views.aide, name='home'),
    path('depot', views.depot, name='depot'),
    path('retrait', views.retrait, name='retrait'),
    path('transfert', views.transfert, name='transfert'),
]