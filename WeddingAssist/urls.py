from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

from WeddingAssist import views
from parties.urls import party_templates_urls

user_urls = patterns('',
    url(r'^$', views.UserList.as_view(), name='user-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
)

template_urls = patterns('',
    url(r'^parties/', include(party_templates_urls)),
)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include(user_urls, namespace='users')),
    url(r'^noters/', include('noters.urls', namespace='noters')),
    url(r'^parties/', include('parties.urls', namespace='parties')),
    url(r'^templates/', include(template_urls, namespace='templates')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
