from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', TaskDetail.as_view()),
    path('', TaskList.as_view())
]