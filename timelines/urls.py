from django.urls import path

from . import views

app_name = 'timelines'
urlpatterns = [
    path('view/<int:id>/', views.timeline_view, name='view'),
    path('view/', views.timeline_list_view, name='list'),
    path('edit/<int:id>/', views.edit_timeline, name='edit'),
    path('delete_event/<int:id>/', views.delete_event, name='delete_event'),
]
