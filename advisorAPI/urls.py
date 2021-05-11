from django.urls import path, include
from .views import addAdvisor, registerUser, loginUser, getAdvisorList

urlpatterns = [
    path('advisor/', addAdvisor),
    path('user/register/', registerUser),
    path('user/login/', loginUser),
    path('user/<int:user_id>/advisor/', getAdvisorList)
    
]