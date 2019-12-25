from django.contrib import admin
from newuser.models import *

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(BuyersProfile)
admin.site.register(SellersProfile)
