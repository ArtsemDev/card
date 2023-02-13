from django.contrib import admin

from .models import *


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_filter = ['status', 'seria', 'id']
    date_hierarchy = 'date_created'
    search_fields = ['id']


admin.site.register(CardStatus)
admin.site.register(CardSeria)
# admin.site.register(Card)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderProduct)
