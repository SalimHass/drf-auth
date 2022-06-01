from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import (
                                        ListCreateAPIView
                                    )
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)