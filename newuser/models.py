from django.db import models
from django.contrib.auth import get_user_model
from store.models import Company



# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.CharField(max_length = 50, null = True, blank = True)

    def __str__(self):
        return self.first_name
    
    def get_json(self):
        return {
            "user" : self.user.username,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "age" : self.age,
            "email" : self.email
        }

class BuyersProfile(models.Model):
    userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.userprofile.first_name

    def get_json(self):
        return {
            "user" : self.userprofile.user.username,
            "first_name" : self.userprofile.first_name,
            "last_name" : self.userprofile.last_name,
            "age" : self.userprofile.age,
        }

class SellersProfile(models.Model):
    userprofile = models.OneToOneField(UserProfile, on_delete = models.CASCADE)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)

    def __str__(self):
        return self.userprofile.first_name
    
    def get_json(self):
        return {
            "user" : self.userprofile.user.username,
            "first_name" : self.userprofile.first_name,
            "last_name" : self.userprofile.last_name,
            "age" : self.userprofile.age,
        }

class Address(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=30)
    street_name = models.CharField(max_length=30)
    locality = models.CharField(max_length=30)
    village = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.IntegerField()

    def __str__(self):
        return self.building_name

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def get_json(self):
        return {
            "user_profile" : self.user_profile.first_name,
            "building_name" : self.building_name,
            "street_name" : self.street_name,
            "locality" : self.locality,
            "village" : self.village,
            "district" : self.district,
            "state" : self.state,
            "pincode" : self.pincode,
        }