
from django.urls import path, include
from .views import *
urlpatterns = [
    path('books/', books, name="Show Books"),
]
