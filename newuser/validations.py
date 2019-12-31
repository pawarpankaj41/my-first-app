import json
from newuser.models import UserProfile, SellersProfile, BuyersProfile, Address
from .models import Company
from datetime import datetime
import re 
from validators import *

def validate_login(params):
    username = params.get("username")
    password = params.get("password")

    if not valid_username(username):
        return False, "Please Provide proper username", None
    if not valid_string(password):
        return False, "Please enter the password", None

    kwargs = {
        "username" : username,
        "password" : password,
    }
    return True, "validation successfully", kwargs

def validate_change_password(params):
    old_password = params.get("old_password")
    new_password = params.get("new_password")
    conf_new_password = params.get("conf_new_password")
    username = params.get("username")
    

    if not valid_string(old_password):
        return False, "Please enter the valid old password", None
    if not valid_string(new_password):
        return False, "Please enter the valid new password", None
    if not valid_string(conf_new_password):
        return False, "Please enter the valid confirm password", None
    if not valid_username(username):
        return False, "Please enter the valid username", None
    

    kwargs = {
        "old_password" : old_password,
        "new_password" : new_password,
        "conf_new_password" : conf_new_password,
        "username" : username
    }
    return True, "validation successfully", kwargs

def validate_forget_password(params):
    new_password = params.get("new_password")
    conf_new_password = params.get("conf_new_password")
    username = params.get("username")
    print(username)
    
    if not valid_string(new_password):
        return False, "Please enter the valid new password", None
    if not valid_string(conf_new_password):
        return False, "Please enter the valid confirm password", None
    if not valid_username(username):
        return False, "Please enter the valid username", None
    
    kwargs = {
        "new_password" : new_password,
        "conf_new_password" : conf_new_password,
        "username" : username
    }
    return True, "validation successfully", kwargs


def validate_create_user_profile(params):
    username = params.get("username")
    password = params.get("password")
    first_name = params.get("first_name")
    last_name = params.get("last_name")
    age = params.get("age")

    if not valid_username(username):
        return False, "Please Provide proper username", None
    if not valid_string(first_name):
        return False, "First Name is Mandatory", None
    if not valid_string(last_name):
        return False, "last Name is Mandatory", None
    if not valid_int(age):
        return False, "age is Mandatory", None
    
    kwargs = {
        "username" : username,
        "password" : password,
        "first_name" : first_name,
        "last_name" : last_name,
        "age" : age
    }
    return True, "validation successfully", kwargs

def validate_create_address(params):
    user_profile_id = params.get("user_profile_id")
    building_name = params.get("building_name")
    street_name = params.get("street_name")
    locality = params.get("locality")
    village = params.get("village")
    district = params.get("district")
    state = params.get("state")
    pincode = params.get("pincode")

    if not valid_int(user_profile_id):
        return False, "user_profile_id is Mandatory", None
    if not valid_string(building_name):
        return False, "Please Provide proper building_name", None
    if not valid_string(street_name):
        return False, "street_name is Mandatory", None
    if not valid_string(locality):
        return False, "locality is Mandatory", None
    if not valid_string(village):
        return False, "village is Mandatory", None
    if not valid_string(district):
        return False, "district is Mandatory", None
    if not valid_string(state):
        return False, "state is Mandatory", None
    if not valid_int(pincode):
        return False, "pincode is Mandatory", None
    
    kwargs = {
        "user_profile_id" : user_profile_id,
        "building_name" : building_name,
        "street_name" : street_name,
        "locality" : locality,
        "village" : village,
        "district" : district,
        "state" : state,
        "pincode" : pincode
    }
    return True, "validation successfully", kwargs


def validate_create_sellersprofile(params):
    user_profile_id = params.get("user_profile_id")
    company_id = params.get("company_id")

    if not valid_int(user_profile_id):
        return False, "user_profile_id is Mandatory", None
    if not valid_int(company_id):
        return False, "company_id is Mandatory", None
    
    kwargs = {
        "user_profile_id" : user_profile_id,
        "company_id" : company_id
    }
    return True, "validation successfully", kwargs

def validate_userprofile_id(params):
    user_profile_id = params.get("user_profile_id")

    if not valid_int(user_profile_id):
        return False, "user_profile_id is Mandatory", None
    return True, "validation successfully", {"user_profile_id" : user_profile_id}

def validate_address_id(params):
    address_id = params.get("address_id")

    if not valid_int(address_id):
        return False, "address_id is Mandatory", None
    return True, "validation successfully", {"address_id" : address_id}

def validate_buyersprofile_id(params):
    buyersprofile_id = params.get("buyersprofile_id")

    if not valid_int(buyersprofile_id):
        return False, "buyersprofile_id is Mandatory", None
    return True, "validation successfully", {"buyersprofile_id" : buyersprofile_id}

def validate_sellersprofile_id(params):
    sellersprofile_id = params.get("sellersprofile_id")

    if not valid_int(sellersprofile_id):
        return False, "sellersprofile_id is Mandatory", None
    return True, "validation successfully", {"sellersprofile_id" : sellersprofile_id}

def validate_update_user_profile(params):
    user_profile_id = params.get("user_profile_id")
    first_name = params.get("first_name")
    last_name = params.get("last_name")
    age = params.get("age")

    if not valid_int(user_profile_id):
        return False, "user_profile_id is Mandatory", None
    # if not valid_username(username):
    #     return False, "Please Provide proper username", None
    if not valid_string(first_name):
        return False, "First Name is Mandatory", None
    if not valid_string(last_name):
        return False, "last Name is Mandatory", None
    if not valid_int(age):
        return False, "age is Mandatory", None
    
    kwargs = {
        "user_profile_id" : user_profile_id,
        # "username" : username,
        # "password" : password,
        "first_name" : first_name,
        "last_name" : last_name,
        "age" : age
    }
    return True, "validation successfully", kwargs

def validate_update_address(params):
    address_id = params.get("address_id")
    # user_profile_id = params.get("user_profile_id")
    building_name = params.get("building_name")
    street_name = params.get("street_name")
    locality = params.get("locality")
    village = params.get("village")
    district = params.get("district")
    state = params.get("state")
    pincode = params.get("pincode")

    if not valid_int(address_id):
        return False, "address_id is Mandatory", None
    # if not valid_int(user_profile_id):
    #     return False, "user_profile_id is Mandatory", None
    if not valid_string(building_name):
        return False, "Please Provide proper building_name", None
    if not valid_string(street_name):
        return False, "street_name is Mandatory", None
    if not valid_string(locality):
        return False, "locality is Mandatory", None
    if not valid_string(village):
        return False, "village is Mandatory", None
    if not valid_string(district):
        return False, "district is Mandatory", None
    if not valid_string(state):
        return False, "state is Mandatory", None
    if not valid_int(pincode):
        return False, "pincode is Mandatory", None
    
    kwargs = {
        "address_id" : address_id,
        # "user_profile_id" : user_profile_id,
        "building_name" : building_name,
        "street_name" : street_name,
        "locality" : locality,
        "village" : village,
        "district" : district,
        "state" : state,
        "pincode" : pincode
    }
    return True, "validation successfully", kwargs
