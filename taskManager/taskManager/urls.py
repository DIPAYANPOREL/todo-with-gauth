from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('todo_app.urls')),
    path('', RedirectView.as_view(url='todo_list/', permanent=False)),
]
