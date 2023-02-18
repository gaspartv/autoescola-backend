from django.urls import path
from app_users.views import UserView

urlpatterns = [
    path("users/", UserView.as_view()),
]
