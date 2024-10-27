"""
URL configuration for innovix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
#adding media folder path(media to svae profile_img)
from django.conf import settings
from django.conf.urls.static import static 
from core import views as core_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',core_views.home,name="home"),
    path('profile/',views.profile,name = "profile"),
    path('rankings/',views.rankings , name = "rankings"),
    path('publish/',core_views.publish,name = "publish"),
    path('signup/',core_views.signup,name = 'signup'),
    path('',core_views.signin,name = 'signin'),
    path('logout/',core_views.logout,name = 'logout'),
    path('like/<uuid:post_id>/', core_views.like_post, name='like-post'),

   
]

#need to add this for defing path of media
urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
