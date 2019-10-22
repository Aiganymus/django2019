from rest_framework import viewsets
from rest_framework import mixins

from core.models import Product, Service
from core.serializers import ProductSerializer, ServiceSerializer
from core.views.permissions import IsAdmin


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(existence=True)


class ProductDetailViewSet(mixins.DestroyModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = (IsAdmin, )

    def get_queryset(self):
        return Product.objects.filter(existence=True)

    # def perform_destroy(self, instance):
    #     instance.existence = False
    #     instance.save()


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class ServiceDetailViewSet(mixins.DestroyModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    permission_classes = (IsAdmin, )

