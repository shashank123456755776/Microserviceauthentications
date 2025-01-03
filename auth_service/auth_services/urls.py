from django.urls import path
from .views import RegisterView, LoginView,ApiKeyLoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/api-key/', ApiKeyLoginView.as_view(), name='api_key_login'),


]
