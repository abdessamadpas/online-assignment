
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('dashboard/', include('core.urls')),
    path('admin/', admin.site.urls),

   #path('', lambda request: redirect('dashboard/', permanent=True)),
]
