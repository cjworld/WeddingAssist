from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from parties import views

party_templates_urls = patterns('',
    url(r'^party-index.html$', TemplateView.as_view(template_name='parties/party-index.html')),
    url(r'^party-list.html$', TemplateView.as_view(template_name='parties/party-list.html')),
    url(r'^party-detail.html$', TemplateView.as_view(template_name='parties/party-detail.html')),
)

user_urls = patterns('',
    url(r'^photos/$', views.UserPhotoList.as_view(), name='userphoto-list'),
    url(r'^parties/$', views.UserPartyList.as_view(), name='userparty-list'),
    url(r'^messages/$', views.UserMessageList.as_view(), name='usermessage-list'),
    url(r'^willingnesses/$', views.UserWillingnessList.as_view(), name='userwillingness-list'),
)

photo_urls = format_suffix_patterns(patterns('',
    url(r'^$', views.PhotoList.as_view(), name='photo-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PhotoDetail.as_view(), name='photo-detail'),
))

party_urls = format_suffix_patterns(patterns('',
    url(r'^$', views.PartyList.as_view(), name='party-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PartyDetail.as_view(), name='party-detail'),
    url(r'^(?P<pk>[0-9]+)/messages$', views.PartyMessageList.as_view(), name='partymessage-list'),
    url(r'^(?P<pk>[0-9]+)/willingnesses$', views.PartyWillingnessList.as_view(), name='partywillingness-list'),
))

message_urls = format_suffix_patterns(patterns('',
    url(r'^$', views.MessageList.as_view(), name='message-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.MessageDetail.as_view(), name='message-detail'),
))

willingness_urls = format_suffix_patterns(patterns('',
    url(r'^$', views.WillingnessList.as_view(), name='willingness-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.WillingnessDetail.as_view(), name='willingness-detail'),
))

api_urlpatterns = patterns('',
    url(r'^user/', include(user_urls)),
    url(r'^photos/', include(photo_urls)),
    url(r'^parties/', include(party_urls)),
    url(r'^messages/', include(message_urls)),
    url(r'^willingnesses/', include(willingness_urls)),
)

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name='parties/party-base.html'), name='base'),
    url(r'^api/', include(api_urlpatterns)),
)