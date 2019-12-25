from django.contrib import admin
from store.models import Company, Region, SubRegion, City, Category, Store, Department, Subcategory, Product, Followership
from django.http import HttpResponse

# Register your models here.
# fields = ( 'image_tag', )
# readonly_fields = ('image_tag',)

# class StoreAdmin(admin.ModelAdmin):

#     readonly_fields = [..., "store_image"]

#     def store_image(self, obj):
#         return HttpResponse('<img src="{url}" width="{width}" height={height} />').format(
#             url = obj.images.url
#             )

# class StoreAdmin(admin.ModelAdmin):
#     # explicitly reference fields to be shown, note image_tag is read-only
#     fields = ( 'image_tag','store_name','store_address', 'store_latitude', 'store_longitude' )
#     readonly_fields = ('image_tag',)




admin.site.register(Company)
admin.site.register(Region)
admin.site.register(SubRegion)
admin.site.register(City)
admin.site.register(Store)
admin.site.register(Department)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)
admin.site.register(Followership)