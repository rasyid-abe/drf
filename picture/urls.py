from django.urls import path
from . import views

urlpatterns = [
    path('', views.PictureListAPIView.as_view(), name='pictures'),
    path('<int:id>', views.PictureDetailAPIView.as_view(), name='picture'),
]
