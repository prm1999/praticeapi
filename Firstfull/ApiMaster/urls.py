from django.urls import path
from .views import *

urlpatterns = [
    path('crop', CropView.as_view()),
    path('crop/<int:id>', CropUpdateView.as_view()),

]