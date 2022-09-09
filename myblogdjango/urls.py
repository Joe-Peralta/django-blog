
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    #Core
    path('', include('AppCore.urls')),
    #Blog
    path('Blogs/', include('AppBlog.urls')),
   #Perfil
    path('perfil/', include('AppPerfil.urls')),
    
]
