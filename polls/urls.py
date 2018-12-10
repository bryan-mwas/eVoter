from django.urls import path
from . import views

# Namespaces help generate precise urls in templates using the {% url %} syntax
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/55/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/55/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/55/votes
    path('<int:question_id>/votes/', views.vote, name='vote'),
]
