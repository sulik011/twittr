from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostAPIView.as_view),
    # path('postlist/<int:pk>/', views.PostDetail.as_view),
]