from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from noters import views

memo_urls = format_suffix_patterns(patterns('',
    url(r'^$', views.MemoList.as_view(), name='memo-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.MemoDetail.as_view(), name='memo-detail'),
))

notebook_urls = format_suffix_patterns(patterns('',
    url(r'^$', views.NotebookList.as_view(), name='notebook-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.NotebookDetail.as_view(), name='notebook-detail'),
))

urlpatterns = patterns('',
    url(r'^$', views.Index, name='index'),
    url(r'^memos/', include(memo_urls)),
    url(r'^notebooks/', include(notebook_urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
'''
memo_list = MemoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
memo_detail = MemoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

notebook_list = NotebookViewSet.as_view({
    'get': 'list'
    'post': 'create'
})
notebook_detail = NotebookViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
'''