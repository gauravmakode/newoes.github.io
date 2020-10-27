from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserList.as_view()),
    path('current', views.current_user),
    path('level/', views.Listuserlevel.as_view()),
]
