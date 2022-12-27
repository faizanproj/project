
from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/', registerview, name='register'),
    path('login/', loginviews, name='login'),
    path('logout/', logoutviews, name='logout'),
    path('appointment/',appointment,name = 'appointment'),
    path('delete/<int:id>/',deletedata,name = 'delete'),
    path('edit/<int:id>/',edit,name = 'edit'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
