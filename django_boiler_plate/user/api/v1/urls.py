from django.urls import include, path
from .views.user import UserAPIView

urlpatterns = [
    path('user/', UserAPIView.as_view(), name="user"),
]
