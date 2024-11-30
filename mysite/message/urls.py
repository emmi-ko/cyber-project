from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='message'),
    path('message/create', views.create_message, name='message-create'),
    path('message/delete/<int:id>/', views.delete_message, name='message-delete'),
]
