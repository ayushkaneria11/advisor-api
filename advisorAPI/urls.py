from django.urls import path, include
from .views import addAdvisor, registerUser, loginUser

urlpatterns = [
    path('advisor/', addAdvisor),
    path('user/register/', registerUser),
    path('user/login/', loginUser)
    
]