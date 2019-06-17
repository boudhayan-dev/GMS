from django.contrib import admin
from .models import Gym , Address, Owner, Equipmet_MT , Equipment_Details, Category_MT, Diet

# Register your models here.
admin.site.register(Address)
admin.site.register(Gym)
admin.site.register(Owner)
admin.site.register(Equipmet_MT)
admin.site.register(Equipment_Details)
admin.site.register(Category_MT)
admin.site.register(Diet)
