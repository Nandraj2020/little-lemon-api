from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, MenuItemViewSet, RegistrationView

router = DefaultRouter()
router.register("menu", MenuItemViewSet, basename="menu")
router.register("bookings", BookingViewSet, basename="booking")

urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("", include(router.urls)),
]
