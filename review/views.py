from django.shortcuts import render

from rest_framework import viewsets
from .models import Review, Hotel
from .serializers import ReviewSerializer, HotelSerializer, SearchReviewFilter, SearchHotelFilter


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class SearchReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_class = SearchReviewFilter


class SearchHotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_class = SearchHotelFilter
