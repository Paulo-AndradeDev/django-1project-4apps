from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    # added the word 'specifics'
    # the 'name' value as called by the {% url %} template tag
    path('', views.IndexView.as_view(), name='index'),

    # ex: /polls/5/results/
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('specifics/<int:question_id>/', views.detail, name='detail'),

    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

"""
app_name = 'polls'
urlpatterns = [
    
    path('', views.index, name='index'),
    # ex: /polls/5/
    # added the word 'specifics'
    # the 'name' value as called by the {% url %} template tag
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
"""