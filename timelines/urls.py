from django.urls import path

from . import views

app_name = 'timelines'
urlpatterns = [
    path('view/<int:id>/', views.timeline_view, name='view'),
    path('view/', views.timeline_list_view, name='list'),
]
