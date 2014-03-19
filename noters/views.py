from rest_framework import generics, permissions, viewsets
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from noters.serializers import MemoSerializer, NotebookSerializer
from noters.models import Memo, Notebook

@login_required
def Index(request):
    context = {}
    return render(request, 'noters/index.html', context)

class MemoList(generics.ListCreateAPIView):
    model = Memo
    serializer_class = MemoSerializer

    def get_queryset(self):
        queryset = super(MemoList, self).get_queryset()
        return queryset.filter(author__username=self.request.user.username)
    
    def pre_save(self, obj):
        obj.author = self.request.user
        return super(MemoList, self).pre_save(obj)

class MemoDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Memo
    serializer_class = MemoSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class NotebookList(generics.ListCreateAPIView):
    model = Notebook
    serializer_class = NotebookSerializer
                          
    def get_queryset(self):
        queryset = super(NotebookList, self).get_queryset()
        return queryset.filter(owner__username=self.request.user.username)

    def pre_save(self, obj):
        obj.owner = self.request.user
        return super(NotebookList, self).pre_save(obj)

class NotebookDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Notebook
    serializer_class = NotebookSerializer
    permission_classes = [
        permissions.AllowAny
    ]