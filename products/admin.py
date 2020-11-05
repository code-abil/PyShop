from django.contrib import admin
from .models import Product, Offer


# Customizing the Admin Dashboard for Product Model:
class ProductAdmin(admin.ModelAdmin):
    # By default, the entries of "product" app are not displayed.
    list_display = ('name', 'price', 'stock')


# admin.site.register(Product)  (Without any customisation)
admin.site.register(Product, ProductAdmin)


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Offer, OfferAdmin)
