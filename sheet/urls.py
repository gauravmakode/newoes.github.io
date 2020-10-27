from django.urls import path
from . import views

urlpatterns = [
    path('level/', views.Listlevel.as_view()),
    path('level/<int:pk>/', views.Detaillevel.as_view()),

    path('subject/', views.Listsubject.as_view()),
    path('subject/<int:pk>/', views.Detailsubject.as_view()),

    path('topic/', views.Listtopic.as_view()),
    path('topic/<int:pk>/', views.Detailtopic.as_view()),

    path('sheetname/', views.Listsheetname.as_view()),
    path('sheetname/<int:pk>/', views.Detailsheetname.as_view()),

    path('questions/', views.Listquestions.as_view()),
    path('questions/<int:pk>/', views.Detailquestions.as_view()),

    path('index/', views.Listindex.as_view()),
    path('index/<int:pk>/', views.Detailindex.as_view()),

    path('useranswers/', views.ListUserAnswers.as_view()),
    path('useranswers/<int:pk>/', views.DetailUserAnswers.as_view()),

    path('flag/', views.Listflag.as_view()),
    path('flag/<int:pk>/', views.Detailflag.as_view()),
]
