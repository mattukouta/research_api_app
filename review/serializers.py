from rest_framework import serializers
from review.models import Review, Hotel
from django_filters import rest_framework as filters


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('sentence', 'hotel', 'purpose', 'companion')


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('HotelID', 'Prefectures', 'Cities', 'address')


class SearchReviewFilter(filters.FilterSet):
    schema_name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Review
        fields = ('sentence', 'hotel', 'purpose', 'companion')


class SearchHotelFilter(filters.FilterSet):
    table_name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Hotel
        fields = ('HotelID', 'Prefectures', 'Cities', 'address')
