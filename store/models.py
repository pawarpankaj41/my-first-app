from django.db import models
from django.conf import settings
import os, json

#from newuser.models import UserProfile

# Create your models here.

# def upload_image(instance, filename):
#     if os.path.isdir(settings.BASE_DIR+'/Media/avtar'):  # will go in if statement, if required directory is exist.
#         return os.path.join('avtar/'+"%s" %(re.sub('[^a-zA-Z0-9 \.\_]', '', filename).replace(' ', ''), ))
#     else:
#         os.makedirs(settings.BASE_DIR+'/Media/avtar')
#         return os.path.join('avtar/'+"%s" %(re.sub('[^a-zA-Z0-9 \.\_]', '', filename).replace(' ', ''), ))


# def image_tag(self):
#     from django.utils.html import escape
#     return u'<img src="%s" />' % escape(<URL to the image>)
# image_tag.short_description = 'Image'
# image_tag.allow_tags = True


class Company(models.Model):
    company_name = models.CharField(max_length = 100)
    financial_start_date = models.DateField()
    financial_end_date = models.DateField()
    joined_date = models.DateTimeField(auto_now_add = True)
    phone = models.IntegerField()
    website = models.URLField(max_length = 100)
    email = models.EmailField(max_length = 100)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def get_json(self):
        data = {
            "company_name" : self.company_name, 
            "financial_start_date" : self.financial_start_date, 
            "financial_end_date" : self.financial_end_date, 
            "joined_date" : self.joined_date, 
            "phone" : self.phone, 
            "website" : self.website, 
            "email" : self.email
        }
        return data


class Region(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null = True, blank = True)
    region_name = models.CharField(max_length = 100, null = True, blank = True)

    def __str__(self):
        return self.region_name

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    def get_json(self):
        return {
                "company" : self.company.company_name,
                "region_name" : self.region_name,
        }



class SubRegion(models.Model):
    company = models.ForeignKey(Company,  related_name= 'company_rel',  on_delete=models.CASCADE, null = True, blank = True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null = True, blank = True)
    subregion_name = models.CharField(max_length = 100, null = True, blank = True)

    def __str__(self):
        return self.subregion_name

    class Meta:
        verbose_name = "SubRegion"
        verbose_name_plural = "SubRegions"

    def get_json(self):
        return {
            "company" : self.company.company_name,
            "region" : self.region.region_name,
            "subregion_name" : self.subregion_name,
        }

class City(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    subregion = models.ForeignKey(SubRegion, on_delete=models.SET_NULL, null = True, blank = True)
    city_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def get_json(self):
        if self.subregion is not None:
            return {
                "company" : self.company.company_name,
                "subregion" : self.subregion.subregion_name,
                "city_name" : self.city_name,
            }
        else:
            return {
                "company" : self.company.company_name,
                "city_name" : self.city_name,
            }

class Store(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null = True, blank = True)
    city = models.ForeignKey(City, on_delete= models.CASCADE, null = True, blank = True)
    store_name = models.CharField(max_length = 300)
    store_address = models.CharField(max_length = 500)
    store_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    store_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    store_image = models.ImageField(upload_to ="images", null = True, blank = True)
    gstin = models.CharField(max_length = 15)
    gstin_certificate = models.FileField(upload_to= "gstin certificates")
    fssai = models.CharField(max_length=14)
    fssai_certificate = models.FileField(upload_to= "fssai certificates")
    followers = models.ManyToManyField('newuser.UserProfile', through= 'Followership')

    def get_json(self):
        data = {
                "company" : self.company.company_name,
                "city" : self.city.city_name,
                "store_name" : self.store_name,
                "store_address" : self.store_address,
                "store_latitude" : self.store_latitude,
                "store_longitude" : self.store_longitude,
                "store_image" : str(self.store_image),
                "gstin" : self.gstin,
                "gstin_certificate" : str(self.gstin_certificate),
                "fssai" : self.fssai,
                "fssai_certificate" : str(self.fssai_certificate),
                "followers" : self.get_followers()
        }
        return data

    def __str__(self):
        return self.store_name

    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "Stores"

    def get_followers(self):
        followers_list = self.followers.all()
        return [{'id': obj.id, 'first_name' : obj.first_name} for obj in followers_list]

    

    # def url(self):
    #     # returns a URL for either internal stored or external image url
    #     if self.externalURL:
    #         return self.externalURL
    #     else:
    #         # is this the best way to do this??
    #         return os.path.join('/',settings.MEDIA_URL, os.path.basename(str(self.image)))
    #         print(str(self.image))

    # def image_tag(self):
    # # used in the admin site model as a "thumbnail"
    #     return mark_safe('<img src="{url}" width="150" height="150" />'.format(self.url()))
  

    # def __unicode__(self):
    # # add __str__() if using Python 3.x
    #     return self.store_name


class Department(models.Model):
    store = models.ForeignKey(Store, on_delete= models.CASCADE)
    department_name = models.CharField(max_length = 100)
    department_image = models.ImageField(upload_to ="images", null = True, blank = True)

    def get_json(self):
        return {
            "store" : self.store.store_name,
            "department_name" : self.department_name,
            "department_image" : str(self.department_image)
        }

    def __str__(self):
        return self.department_name

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"



class Category(models.Model):
    store = models.ForeignKey(Store, on_delete= models.CASCADE)
    department = models.ForeignKey(Department, on_delete= models.CASCADE)
    category_name = models.CharField(max_length = 100)
    category_image = models.ImageField(upload_to ="images", null = True, blank = True)

    def get_json(self):
        return {
            "department" : self.department.department_name,
            "store" : self.store.store_name,
            "category_name" : self.category_name,
            "category_image" : str(self.category_image)
        }

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Subcategory(models.Model):
    store = models.ForeignKey(Store, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    subcategory_name = models.CharField(max_length = 100)
    subcategory_image = models.ImageField(upload_to ="images", null = True, blank = True)

    def get_json(self):
        return {
            "category" : self.category.category_name,
            "store" : self.store.store_name,
            "subcategory_name" : self.subcategory_name,
            "subcategory_image" : str(self.subcategory_image)
        }

    def __str__(self):
        return self.subcategory_name

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete= models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete= models.CASCADE)
    product_name = models.CharField(max_length = 100)
    product_price = models.FloatField(max_length=10)
    product_discount_price = models.FloatField(max_length=10)
    product_quantity = models.IntegerField()
    product_description = models.TextField(max_length = 200)
    product_image = models.ImageField(upload_to ="images", null = True, blank = True)

    def get_json(self):
        return {
            "subcategory" : self.subcategory.subcategory_name,
            "store" : self.store.store_name,
            "product_name" : self.product_name,
            "product_price" : self.product_price,
            "product_discount_price" : self.product_discount_price,
            "product_quantity" : self.product_quantity,
            "product_description" : self.product_description,
            "product_image" : str(self.product_image)
        }

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

class Followership(models.Model):
    Not_interested = 'A'
    High_Prices = 'B'
    Not_liked = 'C'
    

    reason_choices= [
        (Not_interested , 'Not_interested'),
        (High_Prices, 'High_Prices'),
        (Not_liked, 'Not_liked'),
    ]
    users = models.ForeignKey('newuser.UserProfile', on_delete=models.CASCADE, null = True, blank = True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null = True, blank = True)
    remove_reason = models.CharField(max_length = 2, choices = reason_choices, null = True)


    def __str__(self):
        if self.users is None:
            return self.store.store_name
        else:
            return self.store.store_name + " : " + self.users.first_name
        
# class Cart(models.Model):
#     userprofile = models.ForeignKey('newuser.UserProfile', on_delete= models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now= True)
#     total_quantity = models.PositiveIntegerField()
#     total_price = models.FloatField()


# class CartItems(models.Model):
#     cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
#     product = models.ManyToManyField(Product)
#     quantity = models.PositiveIntegerField()
#     color = models.CharField(null= True, blank = True)
#     price = models.FloatField(null= True, blank= True)
    # discount_price = models.FloatField(null=True, blank=True)
    


