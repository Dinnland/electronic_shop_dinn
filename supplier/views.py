from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from supplier.models import Supplier, Product
from supplier.serializers.serializers import SupplierSerializer, ProductSerializer
from users.permissions import IsActiveUser, IsSuperuser


# Create your views here.
class SupplierViewSet(viewsets.ModelViewSet):
    """ Это ViewSet для User """
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['country']
    ordering_fields = ['country']

    def get_serializer_class(self):
        """Обновить поле debt_amount нельзя"""
        serializer_class = self.serializer_class
        if self.request.method in ['PUT', 'PATCH']:
            setattr(serializer_class.Meta, 'read_only_fields', ('debt_amount',))
        return serializer_class

    def get_permissions(self):
        """Удаление только для админа, остальное - активным пользователям"""
        if self.action == 'destroy':
            permission_classes = [IsSuperuser]
        else:
            permission_classes = [IsActiveUser]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        new_supplier = serializer.save()
        if new_supplier.supplier_type == 'factory':
            new_supplier.ranking = '0'
        elif new_supplier.previous_supplier:
            if new_supplier.previous_supplier.ranking == '0':
                new_supplier.ranking = '1'
            elif new_supplier.previous_supplier.supplier_type == 'factory':
                new_supplier.ranking = '1'
            elif new_supplier.previous_supplier.ranking == '1':
                new_supplier.ranking = '2'

        new_supplier.save()

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def perform_update(self, serializer):

        new_supplier = serializer.save()
        if new_supplier.supplier_type == 'factory':
            new_supplier.ranking = '0'
        elif new_supplier.previous_supplier != 'null':
            if new_supplier.previous_supplier.ranking == '0':
                new_supplier.ranking = '1'
            elif new_supplier.previous_supplier.ranking == '1':
                new_supplier.ranking = '2'
        new_supplier.save()

    def perform_destroy(self, instance):
        instance.delete()


class ProductViewSet(viewsets.ModelViewSet):
    """ Это ViewSet для User """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
