from rest_framework import routers
from .views import ReviewViewSet, HotelViewSet, SearchReviewViewSet, SearchHotelViewSet


router = routers.DefaultRouter()
router.register(r'reviews', ReviewViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'review', SearchReviewViewSet)
router.register(r'hotel', SearchHotelViewSet)
urlpatterns = router.urls
