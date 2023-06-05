from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[
    path('', views.Home_Page, name="Home"),
    path('About', views.About_Page, name="About"),
    path('contact', views.Contact_Page, name="Contact"),
    path('news', views.News_Page, name="News"),
    path('rooms', views.Rooms_Page, name="Rooms"),
]

urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)