from django.urls import path

from . import views

app_name = 'timelines'
urlpatterns = [
    path('view/<int:id>/', views.timeline, name='view'),
]
