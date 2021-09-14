from django.contrib import admin

from store.models import Discount


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['book', 'start_date', 'end_date', 'amount',]
 
