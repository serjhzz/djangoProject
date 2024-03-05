from django.urls import path

from my_app.apps import MyAppConfig
from my_app.views import PostView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, PostHome

app_name = MyAppConfig.name

urlpatterns = [
    path('', PostHome.as_view(), name='home'),
    path('posts/', PostView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('view/<int:pk>/', PostDetailView.as_view(), name='view'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
]
