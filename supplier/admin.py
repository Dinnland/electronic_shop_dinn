from django.contrib import admin, messages
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
# from admin.

from supplier.models import Supplier, Product
from supplier.serializers.serializers import SupplierSerializer
from supplier.views import SupplierViewSet



@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'previous_supplier','customer_link', 'debt_amount', 'supplier_type','ranking')
    readonly_fields = ['ranking']
    # SupplierSerializer()
    # SupplierViewSet()
    # list_filter = ('city',)
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

    def customer_link(self, obj):
        print(obj.previous_supplier)
        if obj.previous_supplier:
            # return u'<a href="{0}">{1}</a>'.format(reverse('admin:auth_user_change', args=(obj.previous_supplier.pk,)),
            #                                        obj.customer)
            # path(
            #     "<path:object_id>/change/",
            #     wrap(self.change_view),
            #     name="%s_%s_change" % info,
            # ),
            # return u'<a href="{0}">{1}</a>'.format(reverse('admin:auth_user_change', args=(obj.previous_supplier.pk,)),
            #                                        obj.customer)
            return reverse_lazy(f'http://127.0.0.1:8000/admin/supplier/supplier/{obj.previous_supplier.pk}/patch/')
            return obj.previous_supplier

    customer_link.allow_tags = True
    customer_link.admin_order_field = 'previous_supplier'
    customer_link.short_description = Supplier._meta.get_field('previous_supplier').verbose_name.title()

    # def view_previous_supplier_link(self, obj):
    #     from django.utils.html import format_html
    #     # count = obj.person_set.count()
    #     url = (
    #             reverse("admin:core_previous_supplier_changelist")
    #             + "?"
    #             + urlencode({"previous_supplier__id": f"{obj.id}"})
    #     )
    #     return format_html('<a href="{}">{} Students</a>', url)
    #
    # view_previous_supplier_link.short_description = "Students"

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        print('555')
        for instance in instances:
            print('555')
            if instance.supplier_type == 'factory':
                print('factory=', instance.supplier_type)
                instance.ranking = '0'
            elif instance.previous_supplier:
                if instance.previous_supplier.ranking == '0':
                    instance.ranking = '1'
                elif instance.previous_supplier.ranking == '1':
                    instance.ranking = '2'
            instance.save()
        formset.save_m2m()
    # supplier = Supplier()
    # print(supplier)
    # if supplier.supplier_type == 'factory':
    #     print('factory=', supplier)
    #     supplier.ranking = '0'
    # elif supplier.previous_supplier:
    #     if supplier.previous_supplier.ranking == '0':
    #         supplier.ranking = '1'
    #     elif supplier.previous_supplier.ranking == '1':
    #         supplier.ranking = '2'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ["supplier"]
    list_display = ('name','supplier', 'model', 'launch_date', 'price')


# @admin.register(Contacts)
# class ContactsAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Debt)
# class DebtAdmin(admin.ModelAdmin):
#     pass