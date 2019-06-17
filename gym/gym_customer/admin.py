from django.contrib import admin
from .models import Customer, Diet_Subscription
# Register your models here.
admin.site.register(Customer)
admin.site.register(Diet_Subscription)
# admin.site.register(Address)