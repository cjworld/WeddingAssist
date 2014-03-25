from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from parties import views

photo_urls = format_suffix_patterns(patterns('',
    url(r'^$', views.PhotoList.as_view(), name='photo-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PhotoDetail.as_view(), name='photo-detail'),
))

party_urls = format_suffix_patterns(patterns('',
    url(r'^$', views.PartyList.as_view(), name='party-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PartyDetail.as_view(), name='party-detail'),
))

message_urls = format_suffix_patterns(patterns('',
    url(r'^$', views.MessageList.as_view(), name='message-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.MessageDetail.as_view(), name='message-detail'),
))

participationwillingness_urls = format_suffix_patterns(patterns('',
    url(r'^$', views.ParticipationWillingnessList.as_view(), name='participationwillingness-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.ParticipationWillingnessDetail.as_view(), name='participationwillingness-detail'),
))

urlpatterns = patterns('',
    #url(r'^$', views.Index, name='index'),
	url(r'^photos/', include(photo_urls)),
    url(r'^parties/', include(party_urls)),
	url(r'^messages/', include(message_urls)),
	url(r'^participationwillingnesses/', include(participationwillingness_urls)),
)