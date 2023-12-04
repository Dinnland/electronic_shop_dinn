from django.contrib import admin, messages
from django.urls import reverse
from supplier.models import Supplier, Product

from django.utils.html import format_html


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'supplier_link', 'debt_amount', 'supplier_type', 'ranking')
    readonly_fields = ['ranking', 'supplier_link']
    search_fields = ("name",)
    list_filter = ["city", "country"]
    actions = ("clear_the_debt",)  # Necessary

    @admin.action(description='Очистить задолженность')
    def clear_the_debt(modeladmin, request, queryset):
        for obj in queryset:
            obj.debt_amount = 0
            obj.save()
            messages.success(request, "Очистка прошла успешно!")

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if instance.supplier_type == 'factory':
                instance.ranking = '0'
            elif instance.previous_supplier:
                if instance.previous_supplier.ranking == '0':
                    instance.ranking = '1'
                elif instance.previous_supplier.ranking == '1':
                    instance.ranking = '2'
            instance.save()
        formset.save()

    def supplier_link(self, obj):
        """Получение ссылки на поставщика"""
        prev_supp = obj.previous_supplier
        if prev_supp is not None:
            filter_supplier = Supplier.objects.filter(name=prev_supp.name)
            prev_supp_pk = filter_supplier.first().pk
            link = reverse('admin:supplier_supplier_changelist')
            return format_html(f'<a href="{prev_supp_pk}">{obj.previous_supplier}</a>', link)
    supplier_link.short_description = 'Поставщик оборудования'  # Column header


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ["supplier"]
    list_display = ('name', 'supplier', 'model', 'launch_date', 'price')
