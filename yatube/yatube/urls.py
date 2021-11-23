from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('posts.urls', namespace='main')),
    # path('', include(('posts.urls', 'posts'), namespace='posts')),
    # path('', include('posts.urls', 'profile'), namespace='profile'),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('about/', include('about.urls', namespace='about')),
]
