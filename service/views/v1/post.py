from rest_framework import viewsets, pagination
from service.authentication import BaseSessionAuthentication
from service.models import Region, Post
from service.serializers import RegionSerializer, PostSerializer


class PostPagination(pagination.PageNumberPagination):
    page_size = 20


class RegionViewSet(viewsets.ModelViewSet):
    authentication_classes = (
        BaseSessionAuthentication,
    )

    http_method_names = ['get']

    serializer_class = RegionSerializer
    queryset = Region.objects.all()

    def get_queryset(self):
        return Region.objects.filter().order_by('city')


class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = (
        BaseSessionAuthentication,
    )
    pagination_class = PostPagination
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        return Post.objects.order_by('-created_at')

