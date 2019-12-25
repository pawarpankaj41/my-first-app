from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db import transaction
from django.contrib.auth import get_user_model
from .validations import *
from .helpers import *
from .models import UserProfile, Address, BuyersProfile, SellersProfile
from store.models import Company
from django.core.exceptions import ObjectDoesNotExist


def create_user_profile_function(data):
    try:
        with transaction.atomic():
            user = get_user_model().objects.create(username = data["username"])
            user.set_password(data["password"])
            user.save()
            user_data = UserProfile.objects.create(
                user = user,
                first_name = data["first_name"],
                last_name = data["last_name"],
                age = data["age"]
            )
        return {"user data": user_data}, True
    except Exception as e:
        print(e)
        return None, False

def create_address_function(data):
    try:
        with transaction.atomic():
            userprofile = UserProfile.objects.get(id = data["user_profile_id"])
            address_data = Address.objects.create(
                user_profile = userprofile ,
                building_name =data["building_name"],
                street_name =data["street_name"],
                locality =data["locality"],
                village =data["village"],
                district =data["district"],
                state =data["state"] ,
                pincode =data["pincode"]
            )
        return {"address data": address_data}, True
    except Exception as e:
        print(e)
        return None, False

def create_buyersprofile_function(data):
    try:
        with transaction.atomic():
            userprofile = UserProfile.objects.get(id = data["user_profile_id"])
            buyers_data = BuyersProfile.objects.create(
                userprofile = userprofile,
            )
        return {"buyers data": buyers_data}, True
    except Exception as e:
        print(e)
        return None, False

def create_sellersprofile_function(data):
    try:
        with transaction.atomic():
            userprofile = UserProfile.objects.get(id = data["user_profile_id"])
            company = Company.objects.get(id = data["company_id"])
            sellers_data = SellersProfile.objects.create(
                userprofile = userprofile,
                company = company
            )
        return {"sellers data": sellers_data}, True
    except Exception as e:
        print(e)
        return None, False

def get_user_by_id_function(data):
    try:
        userprofile_data = UserProfile.objects.get(id = data["user_profile_id"])
        print(userprofile_data)
        data = userprofile_data.get_json()
        return data, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)
    
def get_address_by_userprofile_id_function(data):
    try:
        response = []
        userprofile = UserProfile.objects.get(id = data["user_profile_id"])
        print(userprofile)
        address_data = Address.objects.filter(user_profile = userprofile)
        print(address_data)
        for obj in address_data:
            response.append(obj.get_json())
        return response, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)

def get_buyersprofile_by_id_function(data):
    try:
        buyersprofile_data = BuyersProfile.objects.get(id = data["buyersprofile_id"])
        data = buyersprofile_data.get_json()
        return data, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)

def get_sellersprofile_by_id_function(data):
    try:
        sellersprofile_data = SellersProfile.objects.get(id = data["sellersprofile_id"])
        data = sellersprofile_data.get_json()
        return data, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)

def get_all_userprofile_function():
    data = []
    try:
        userprofile_data = UserProfile.objects.all()
        for obj in userprofile_data:   
            data.append(obj.get_json())
        return data, True, "Successful"
    except Exception as e:
        print(e)
        return None, False, str(e)

def get_all_buyersprofile_function():
    data = []
    try:
        buyersprofile_data = BuyersProfile.objects.all()
        for obj in buyersprofile_data:   
            data.append(obj.get_json())
        return data, True, "Successful"
    except Exception as e:
        print(e)
        return None, False, str(e)

def get_all_sellersprofile_function():
    data = []
    try:
        sellersprofile_data = SellersProfile.objects.all()
        for obj in sellersprofile_data:   
            data.append(obj.get_json())
        return data, True, "Successful"
    except Exception as e:
        print(e)
        return None, False, str(e)

def update_userprofile_function(data):
    try:
        with transaction.atomic():
            userprofile_data = UserProfile.objects.get(id=data["user_profile_id"])
            print(userprofile_data)
            userprofile_data.first_name = data["first_name"]
            userprofile_data.last_name = data["last_name"]
            userprofile_data.age = data["age"]
            userprofile_data.save()
        return {"userprofile data": userprofile_data}, True
    except Exception as e:
        print(e)
        return None, False

def update_address_function(data):
    try:
        with transaction.atomic():
            address_data = Address.objects.get(id=data["address_id"])
            address_data.building_name = data["building_name"] 
            address_data.street_name = data["street_name"] 
            address_data.locality = data["locality"] 
            address_data.village = data["village"] 
            address_data.district = data["district"] 
            address_data.state = data["state"] 
            address_data.pincode = data["pincode"] 
            address_data.save()
        return {"address data": address_data}, True
    except Exception as e:
        print(e)
        return None, False