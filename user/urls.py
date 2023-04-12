from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.regis),
    path('register', views.regis),
    path('login', views.login_page),
    path('logout', views.logout_user),
    path('index', views.index),
    path('upload', views.upload, name='upload'),
    path('like-post', views.like_post, name='like-post'),
    path('delete', views.delete),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)