from rest_framework import generics, permissions, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .models import Booking, MenuItem
from .permissions import IsStaffOrReadOnly
from .serializers import BookingSerializer, MenuItemSerializer, RegistrationSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all().order_by("id")
    serializer_class = MenuItemSerializer
    permission_classes = [IsStaffOrReadOnly]

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Staff can review all bookings; regular users see only their own.
        if self.request.user.is_staff:
            return Booking.objects.all().order_by("booking_date")
        return Booking.objects.filter(user=self.request.user).order_by("booking_date")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "user": {"id": user.id, "username": user.username, "email": user.email},
            "token": token.key,
        }, status=status.HTTP_201_CREATED)
