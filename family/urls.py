from django.urls import path
from . import views

app_name = 'family'

urlpatterns = [
    # этот маршрут отвечает за http://127.0.0.1:8000/tree/
    path('tree/', views.tree, name='tree'),


    path('person/<int:pk>/', views.person_detail, name='person_detail'),

]
