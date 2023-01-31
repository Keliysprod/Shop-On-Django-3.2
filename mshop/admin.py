from django.contrib import admin
from .models import Product,Customer,Order,OrderItem,ShippingAddress


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'digital',)
    list_filter = ('price',)
admin.site.register(Product,ProductAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
    list_filter = ('email',)
admin.site.register(Customer,CustomerAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date_order', 'complete')
    list_filter = ('date_order',)
admin.site.register(Order,OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_added',)
    list_filter = ('date_added',)
admin.site.register(OrderItem,OrderItemAdmin)


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer','address', 'zipcode', 'date_added')
    list_filter = ('date_added','address')
admin.site.register(ShippingAddress,ShippingAddressAdmin)