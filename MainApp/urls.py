from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'MainApp'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('pizza', views.pizza, name = 'pizza'),
    path('indiv_pizza/<int:pizza_id>/', views.indiv_pizza, name = 'indiv_pizza'),
]

urlpatterns += staticfiles_urlpatterns()