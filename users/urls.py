from django.urls import path , include
from .views import *


urlpatterns = [
    path('register/' ,RegisterAPI.as_view()),
    path('freelance/' ,FreelancerRegistration.as_view()),
    path('education/' ,EducationAPI.as_view()),
    path('skills/' ,SkillsAPI.as_view()),
    path('portfolio/' ,PortfolioAPI.as_view()),
    path('certification/' ,CertificationAPI.as_view()),
]
