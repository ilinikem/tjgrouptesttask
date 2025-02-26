from django.urls import path
from .views import department_tree

app_name = 'employees'

urlpatterns = [
    path('', department_tree, name="department_tree"),
]
