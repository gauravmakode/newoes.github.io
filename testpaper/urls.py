from django.urls import path
from . import views

urlpatterns = [
    path('exam/', views.Listexam.as_view()),
    path('exam/<int:pk>/', views.Detailexam.as_view()),

    path('testpaper/', views.ListTestPaper.as_view()),
    path('testpaper/<int:pk>/', views.DetailTestPaper.as_view()),

    path('questions/', views.Listquestions.as_view()),
    path('questions/<int:pk>/', views.Detailquestions.as_view()),

    path('testindex/', views.ListTestIndex.as_view()),
    path('testindex/<int:pk>/', views.DetailTestIndex.as_view()),

    path('useranswers/', views.ListUserAnswers.as_view()),
    path('useranswers/<int:pk>/', views.DetailUserAnswers.as_view()),

    path('userresult/', views.ListUserResult.as_view()),
    path('userresult/<int:pk>/', views.DetailUserResult.as_view()),

    path('flag/', views.Listflag.as_view()),
    path('flag/<int:pk>/', views.Detailflag.as_view()),

    path('timer/', views.Listtimer.as_view()),
    path('timer/<int:pk>/', views.Detailtimer.as_view()),
]
