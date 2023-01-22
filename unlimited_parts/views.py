from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from unlimited_parts.models import Part
from unlimited_parts.models import DescriptionWordCount
from unlimited_parts.serializers import PartSerializer
from unlimited_parts.serializers import DescriptionWordCountSerializer


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 10


class PartViewSet(ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    pagination_class = Pagination


class DescriptionWordCountView(ModelViewSet):
    http_method_names = ["get"]
    # Return top five words with highest count (greater than zero)
    queryset = DescriptionWordCount.objects.order_by("-count", "word").filter(
        count__gt=0
    )[:5]
    serializer_class = DescriptionWordCountSerializer
