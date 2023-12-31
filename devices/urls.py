from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gadgets/', include('gadgets.urls')),
    path('', lambda request: redirect('gadget_list')),  # Redirect root to gadget_list
]
