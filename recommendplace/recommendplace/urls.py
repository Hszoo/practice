from django.contrib import admin
from django.urls import path, include
import app1.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app1.views.home, name="home"),
    path('menus/', include('menus.urls')),
    path('savaplaces/', include('saveplaces.urls')),
]
