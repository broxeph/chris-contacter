from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ConversationCreateView.as_view(), name='conversation-create'),
    path('conversations/', views.ConversationListView.as_view(), name='conversation-list'),
]
