from django.urls import path
from .views import *

urlpatterns = [
    path('manage/',studentmanage),
    path('update/<int:id>/',update,name="update"),
    path('delete/<int:id>/',delete,name="delete"),
    path('add/',addpage,name="addpage")
]
