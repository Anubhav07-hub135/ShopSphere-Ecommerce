from django.contrib import admin
from .models import Category, Product, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug'
    ]

    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'category',
        'price',
        'stock',
        'available',
        'created'
    ]

    list_filter = [
        'available',
        'category',
        'created'
    ]

    list_editable = [
        'price',
        'stock',
        'available'
    ]

    prepopulated_fields = {
        'slug': ('name',)
    }

    search_fields = [
        'name',
        'description'
    ]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = [
        'product',
        'price',
        'quantity'
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'phone',
        'created',
        'paid'
    ]

    list_filter = [
        'paid',
        'created'
    ]

    search_fields = [
        'name',
        'email',
        'phone'
    ]

    inlines = [
        OrderItemInline
    ]