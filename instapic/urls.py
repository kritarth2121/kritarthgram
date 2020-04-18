
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
path('admin/', admin.site.urls),
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^sign-up$', views.signup),
    url(r'^logout$', views.logout),
    url(r'^(?P<username>[a-zA-Z0-9_]+)$', views.profile),
    url(r'^ajax-sign-up$', views.ajaxsignup),
    url(r'^ajax-login$', views.ajaxlogin),
    url(r'^ajax-save-photo$', views.ajaxsavephoto),
    url(r'^ajax-set-profile-pic$', views.ajaxsetprofilepic),
    url(r'^ajax-profile-feed$', views.ajaxprofilefeed),
    url(r'^ajax-like-photo$', views.ajaxlikephoto),
    url(r'^ajax-follow$', views.ajaxfollow),
    url(r'^ajax-tag$', views.ajaxtag),
    url(r'^ajax-photo-feed$', views.ajaxphotofeed)
]
