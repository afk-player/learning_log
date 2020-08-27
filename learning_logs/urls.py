"""Define URL schemas for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Topics pages
    path('topics/', views.topics, name='topics'),
    # Detail topic page
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # New form page
    path('new_topic/', views.new_topic, name='new_topic'),
    # New entry page
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]
