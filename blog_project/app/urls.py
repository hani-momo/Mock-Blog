from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'), # функция, которая будет обрабатывать запрос по этому маршруту
]

