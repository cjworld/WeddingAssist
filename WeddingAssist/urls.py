from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from WeddingAssist import views

user_urls = patterns('',
    url(r'^$', views.UserList.as_view(), name='user-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include(user_urls, namespace='users')),
    url(r'^noters/', include('noters.urls', namespace='noters')),
)
