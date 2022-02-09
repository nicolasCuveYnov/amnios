from django.contrib import admin
from api import models

# Register your models here.

admin.site.register(models.Agency)
admin.site.register(models.Seller)
admin.site.register(models.Buyer)
admin.site.register(models.EstateAgent)
admin.site.register(models.Estate)
admin.site.register(models.VisitSlot)
