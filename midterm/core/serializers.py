from rest_framework import serializers

from core.choices import PRODUCT_SMALL, PRODUCT_GIANT
from core.models import ProductServiceBase, Product, Service


class ProductServiceBaseSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(read_only=True)

    class Meta:
        model = ProductServiceBase
        fields = ('name', 'price', 'description', 'created_at')


class ProductSerializer(ProductServiceBaseSerializer):
    class Meta(ProductServiceBaseSerializer.Meta):
        model = Product
        fields = ProductServiceBaseSerializer.Meta.fields + ('id', 'size', 'type')

    def validate_size(self, value):
        if PRODUCT_SMALL < value > PRODUCT_GIANT:
            raise serializers.ValidationError('size options: [20, 30, 40, 50]')
        return value


class ServiceSerializer(ProductServiceBaseSerializer):
    class Meta(ProductServiceBaseSerializer.Meta):
        model = Service
        fields = ProductServiceBaseSerializer.Meta.fields + ('id', 'approximate_duration', 'service_type')

    def validate_approximate_duration(self, value):
        if value < 0:
            raise serializers.ValidationError('approximate duration must be positive number (hours)')
        return value
