from django.urls import path, include
from rest_framework.routers import DefaultRouter
from unlimited_parts import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"parts", views.PartViewSet, basename="parts")
router.register(
    r"top_part_description_words",
    views.DescriptionWordCountView,
    basename="top_part_description_words",
)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
