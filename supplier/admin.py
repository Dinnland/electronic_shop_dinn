from django.contrib import admin, messages
from django.urls import reverse
from supplier.models import Supplier, Product

from django.utils.html import format_html


# @admin.register(Supplier)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'previous_supplier', 'debt_amount', 'supplier_type', 'ranking')
    # list_display = ('name','supplier_link', 'previous_supplier', 'debt_amount', 'supplier_type', 'ranking')
    readonly_fields = ['ranking']
    # readonly_fields = ['ranking', 'supplier_link']
    search_fields = ("name",)
    list_filter = ["city", "country"]
    # inlines = ['previous_supplier',]
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


#     def user_link(self, obj):
#         return mark_safe('<a href="{}">{}</a>'.format(
#             reverse("admin:auth_user_change", args=(obj.user.pk,)),
#             obj.user.email
#         ))
#
#     user_link.short_description = 'user'
#
# admin.site.register(Supplier, SupplierAdmin)
#     def supplier_link(self, obj):
#         # Generate a link to the related Book admin page for the author
#         # print(obj.previous_supplier)
#         # print(type(obj.previous_supplier))
#         j = obj.previous_supplier
#         if j != 'None':
#             print('j',j)
#         # print('get(name=j)', Supplier.objects.get(name=j))
#         print('filter(name=j)', Supplier.objects.filter(name=j))
#         if Supplier.objects.filter(name=j).exists():
#             print(Supplier.objects.filter(name=j))
#         # if obj.previous_supplier != 'None':
#             # print(obj)
#         object_id = 17
#         # link = reverse('admin:supplier_supplier_changelist') + f'?supplier_id={obj.previous_supplier}'
#         # return format_html(f'<a href="{object_id}">{obj.previous_supplier}</a>', link, object_id=17)
#         #
#         link = reverse('admin:supplier_supplier_changelist') + f'?supplier_id={17}'
#         return format_html(f'<a href="{object_id}">{obj.previous_supplier}</a>', link)
#
#     supplier_link.short_description = 'Поставщик оборудования'  # Column header


admin.site.register(Supplier, SupplierAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ["supplier"]
    list_display = ('name', 'supplier', 'model', 'launch_date', 'price')
