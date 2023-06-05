from django.urls import path
from RegisterLoginApp.views import Register_Page

urlpatterns = [
    path('Register/', Register_Page, name="Register")
]
