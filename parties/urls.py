from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from parties import views

party_templates_urls = patterns('',
    url(r'^party-index.html$', TemplateView.as_view(template_name='parties/party-index.html')),
    url(r'^party-list.html$', TemplateView.as_view(template_name='parties/party-list.html')),
    url(r'^party-detail.html$', TemplateView.as_view(template_name='parties/party-detail.html')),
)

photo_urls = format_suffix_patterns(patterns('',
    url(r'^$', views.PhotoList.as_view(), name='photo-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PhotoDetail.as_view(), name='photo-detail'),
))

party_urls = format_suffix_patterns(patterns('',
    url(r'^$', views.PartyList.as_view(), name='party-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PartyDetail.as_view(), name='party-detail'),
	url(r'^(?P<pk>[0-9]+)/messages$', views.PartyMessageList.as_view(), name='partymessage-list'),
    url(r'^(?P<pk>[0-9]+)/participationwillingness$', views.PartyParticipationWillingnessDetail.as_view(), name='partyparticipationwillingness-detail'),
))

message_urls = format_suffix_patterns(patterns('',
    url(r'^$', views.MessageList.as_view(), name='message-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.MessageDetail.as_view(), name='message-detail'),
))

participationwillingness_urls = format_suffix_patterns(patterns('',
    url(r'^$', views.ParticipationWillingnessList.as_view(), name='participationwillingness-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.ParticipationWillingnessDetail.as_view(), name='participationwillingness-detail'),
))

user_urls = format_suffix_patterns(patterns('',
    url(r'^participationwillingnesses$', views.UserParticipationWillingnessList.as_view(), name='userparticipationwillingness-list'),
    url(r'^parties$', views.UserPartyList.as_view(), name='userparty-list'),
))

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='parties/party-base.html'), name='base'),
	url(r'^photos/', include(photo_urls)),
    url(r'^parties/', include(party_urls)),
	url(r'^messages/', include(message_urls)),
	url(r'^participationwillingnesses/', include(participationwillingness_urls)),
    url(r'^user/', include(user_urls)),
    
)