from rest_framework import serializers
from supplier.models import Supplier, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # validators = [VideoUrlValidator(fields=['video_url'])]


class SupplierSerializer(serializers.ModelSerializer):
    count_of_products = serializers.SerializerMethodField()
    ranking = serializers.CharField(read_only=True)
    products = ProductSerializer(source='product_set', many=True, read_only=True)
    previous_supplier_name = serializers.SerializerMethodField()
    # debt_amount = serializers.CharField(read_only=True)

    class Meta:
        model = Supplier
        fields = '__all__'
        # fields = ("name", "previous_supplier", "supplier_type", "image")

    def get_count_of_products(self, instance):
        """Вывод количества продуктов"""
        if instance.product_set:
            return instance.product_set.all().count()
        else:
            return 0

    def get_previous_supplier_name(self, instance):
        """Вывод названия поставщика оборудования"""
        if instance.previous_supplier:
            return instance.previous_supplier.name
