from rest_framework import viewsets

from unlimited_parts.models import Part
from unlimited_parts.serializers import PartSerializer


class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
