import json
from newuser.models import UserProfile
from .models import Store, Department, Category, Subcategory, Product, Followership
from datetime import datetime
import re 
from validators import *


#----------------------------VALIDATE CREATE COMPANY--------------------------------------
def validate_create_company(params):
    company_name = params.get("company_name")
    financial_start_date = params.get("financial_start_date")
    financial_end_date = params.get("financial_end_date")
    phone = params.get("phone")
    website = params.get("website")
    email = params.get("email")
    
    if not valid_string(company_name):
        return False, "company name is mandatory", None
    if not valid_date_format(financial_start_date):
        return False, "Incorrect date format, should be YYYY-MM-DD", None
    if not valid_date_format(financial_end_date):
        return False, "Incorrect date format, should be YYYY-MM-DD", None
    if not valid_phone(phone):
        return False, "Please Enter Valid Phone Number", None
    if not valid_string(website):
        return False, "Website is mandatory", None
    if not valid_email(email):
        return False, "Please enter a proper email", None
    kwargs = {
        "company_name" : company_name,
        "financial_start_date" : financial_start_date,
        "financial_end_date" : financial_end_date,
        "phone" : phone,
        "website" : website,
        "email" : email
    }
    return True, "validation successfully", kwargs
#----------------------------VALIDATE CREATE REGION--------------------------------------
def validate_create_region(params):
    company_id = params.get("company_id")
    region_name = params.get("region_name")

    if not valid_int(company_id):
        return False, "Company id is mandatory", None
    if not valid_string(region_name):
        return False, "Region name is mandatory", None
    kwargs = {
        "company_id" :company_id,
        "region_name" :region_name
    }
    return True, "validation successfully", kwargs
#----------------------------VALIDATE CREATE SUBREGION--------------------------------------
def validate_create_subregion(params):
    company_id = params.get("company_id")
    region_id = params.get("region_id")
    subregion_name = params.get("subregion_name")
    

    if not valid_int(company_id):
        return False, "Company id is mandatory", None
    if not valid_int(region_id):
        return False, "Region id is mandatory", None
    if not valid_string(subregion_name):
        return False, "Region name is mandatory", None
    kwargs = {
        "company_id" :company_id,
        "region_id" : region_id,
        "subregion_name" :subregion_name
    }
    return True, "validation successfully", kwargs
#----------------------------VALIDATE CREATE CITY--------------------------------------
def validate_create_city(params):
    company_id = params.get("company_id")
    subregion_id = params.get("subregion_id", None)
    city_name = params.get("city_name")
    
    if not valid_int(company_id):
        return False, "Company id is mandatory", None
    if not valid_string(city_name):
        return False, "City name is mandatory", None
    kwargs = {
        "company_id" :company_id,
        "subregion_id" : subregion_id,
        "city_name" :city_name
    }
    return True, "validation successfully", kwargs
#----------------------------VALIDATE CREATE STORE--------------------------------------
def validate_create_store(request):
    try:
        params = request.POST
        print(params)
       
        company_id = int(params.get("company_id"))
        city_id = int(params.get("city_id"))
        store_name = params.get("store_name")
        store_address = params.get("store_address")
        store_latitude = float(params.get("store_latitude"))
        store_longitude = float(params.get("store_longitude"))
        store_image = request.FILES.get("store_image")
        print(store_image)
        gstin = params.get("gstin")
        gstin_certificate = request.FILES.get("gstin_certificate")
        print("gstin_certificate", gstin_certificate)
        fssai = int(params.get("fssai"))
        fssai_certificate = request.FILES.get("fssai_certificate")
        print("fssai_certificate", fssai_certificate)
        
        if not valid_int(company_id):
            return False, "Company id is mandatory", None
        if not valid_int(city_id):
            return False, "City id is mandatory", None
        if not valid_string(store_name):
            return False, "Store name is mandatory", None
        if not valid_string(store_address):
            return False, "Store address is mandatory", None
        if not valid_float(store_latitude):
            return False, "Store_latitude is mandatory", None
        if not valid_float(store_longitude):
            return False, "Store_longitude is mandatory", None
        if not valid_gstin(gstin):
            return False, "Please enter Proper gstin number", None
        if not valid_csv_format(gstin_certificate):
            return False, "Upload Valid CSV file", None
        if not valid_fssai(fssai):
            return False, "Please enter Proper fssai number", None
        if not valid_csv_format(fssai_certificate):
            return False, "Upload Valid CSV file", None
        if not valid_image_format(store_image):
            return False, "Upload Valid image file", None
        kwargs = {
            "company_id" :company_id,
            "city_id" : city_id,
            "store_name" :store_name,
            "store_address" : store_address,
            "store_latitude" : store_latitude,
            "store_longitude" : store_longitude,
            "gstin" : gstin,
            "gstin_certificate" : gstin_certificate,
            "fssai" : fssai,
            "fssai_certificate" : fssai_certificate,
            "store_image" : store_image,
        }
    except Exception as e:
        print(e)
        return False, str(e), None
    return True, "validation successfully", kwargs
#----------------------------VALIDATE CREATE DEPARTMENT--------------------------------------
def validate_create_department(request):
    try:
        params = request.POST
        store_id = int(params.get("store_id"))
        department_name = params.get("department_name")
        department_image = request.FILES.get("department_image")
        if not valid_int(store_id):
            return False, "Store id is mandatory", None
        if not valid_string(department_name):
            return False, "Department name is mandatory", None
        if not valid_image_format(department_image):
            return False, "Upload Valid image file", None
    
        kwargs = {
            "store_id" :store_id,
            "department_name" :department_name,
            "department_image" : department_image
        }
    except Exception as e:
        print(e)
        return False, str(e), None
    return True, "validation successfully", kwargs
#----------------------------VALIDATE CREATE CATEGORY--------------------------------------
def validate_create_category(request):
    try:
        params = request.POST
        store_id = int(params.get("store_id"))
        department_id = int(params.get("department_id"))
        category_name = params.get("category_name")
        category_image = request.FILES.get("category_image")
    
        if not valid_int(store_id):
            return False, "Store id is mandatory", None
        if not valid_int(department_id):
            return False, "department id is mandatory", None
        if not valid_string(category_name):
            return False, "category name is mandatory", None
        if not valid_image_format(category_image):
            return False, "Upload Valid image file", None
    
        kwargs = {
            "store_id" :store_id,
            "department_id" : department_id,
            "category_name" :category_name,
            "category_image" : category_image
        }
    except Exception as e:
        print(e)
        return False, str(e), None
    return True, "validation successfully", kwargs
#----------------------------VALIDATE CREATE SUBCATEGORY--------------------------------------
def validate_create_subcategory(request):
    try:
        params = request.POST
        store_id = int(params.get("store_id"))
        category_id = int(params.get("category_id"))
        subcategory_name = params.get("subcategory_name")
        subcategory_image = request.FILES.get("subcategory_image")
    
        if not valid_int(store_id):
            return False, "Store id is mandatory", None
        if not valid_int(category_id):
            return False, "category id is mandatory", None
        if not valid_string(subcategory_name):
            return False, "subcategory name is mandatory", None
        if not valid_image_format(subcategory_image):
            return False, "Upload Valid image file", None
        
        kwargs = {
            "store_id" :store_id,
            "category_id" : category_id,
            "subcategory_name" :subcategory_name,
            "subcategory_image" : subcategory_image
        }
    except Exception as e:
        print(e)
        return False, str(e), None
    return True, "validation successfully", kwargs
#----------------------------VALIDATE CREATE PRODUCT--------------------------------------
def validate_create_product(request):
    try:
        params = request.POST
        store_id = int(params.get("store_id"))
        subcategory_id = int(params.get("subcategory_id"))
        product_name = params.get("product_name")
        product_price = float(params.get("product_price"))
        product_discount_price = float(params.get("product_discount_price"))
        product_quantity = int(params.get("product_quantity"))
        product_description = params.get("product_description")
        product_image = request.FILES.get("product_image")

        if not valid_int(store_id):
            return False, "Store id is mandatory", None
        if not valid_int(subcategory_id):
            return False, "subcategory id is mandatory", None
        if not valid_string(product_name):
            return False, "product name is mandatory", None
        if not valid_float(product_price):
            return False, "product_price is mandatory", None
        if not valid_float(product_discount_price):
            return False, "product_discount_price is mandatory", None
        if not valid_int(product_quantity):
            return False, "Product quantity is mandatory", None
        if not valid_string(product_description):
            return False, "product_description is mandatory", None
        if not valid_image_format(product_image):
            return False, "Upload Valid image file", None
        
        kwargs = {
            "store_id" :store_id,
            "subcategory_id" : subcategory_id,
            "product_name" :product_name,
            "product_price" : product_price,
            "product_discount_price" : product_discount_price,
            "product_quantity" : product_quantity,
            "product_description" : product_description,
            "product_image" : product_image
        }
    except Exception as e:
        print(e)
        return False, str(e), None
    return True, "validation successfully", kwargs
#---------------------------VALIDATE GET COMPANY BY ID-------------------------------------------------------------
def validate_get_company_by_id(params):
    company_id = int(params.get("company_id"))
    
    if not valid_int(company_id):
        return False, "Company id is mandatory", None
    
    kwargs = {
        "company_id" :company_id,
    }
    return True, "validation successfully", kwargs
#---------------------------VALIDATE GET REGION BY ID--------------------------------------------
def validate_get_region_by_id(params):
    region_id = int(params.get("region_id"))
    
    if not valid_int(region_id):
        return False, "region id is mandatory", None
    kwargs = {
        "region_id" :region_id,
    }
    return True, "validation successfully", kwargs
#---------------------------VALIDATE GET SUBREGION BY ID--------------------------------------------
def validate_get_subregion_by_id(params):
    subregion_id = int(params.get("subregion_id"))
    
    if not valid_int(subregion_id):
        return False, "subregion id is mandatory", None
    
    kwargs = {
        "subregion_id" :subregion_id,
    }
    return True, "validation successfully", kwargs
#---------------------------VALIDATE GET CITY BY ID--------------------------------------------
def validate_get_city_by_id(params):
    city_id = int(params.get("city_id"))
    
    if not valid_int(city_id):
        return False, "city id is mandatory", None
    
    kwargs = {
        "city_id" :city_id,
    }
    return True, "validation successfully", kwargs
#---------------------------VALIDATE GET STORE BY ID--------------------------------------------
def validate_get_store_by_id(params):
    store_id = int(params.get("store_id"))
    
    if not valid_int(store_id):
        return False, "store id is mandatory", None
    
    kwargs = {
        "store_id" :store_id,
    }
    return True, "validation successfully", kwargs
#---------------------------VALIDATE GET DEPARTMENT BY ID--------------------------------------------
def validate_get_department_by_id(params):
    department_id = int(params.get("department_id"))
    
    if not valid_int(department_id):
        return False, "department id is mandatory", None
    
    kwargs = {
        "department_id" :department_id,
    }
    return True, "validation successfully", kwargs
#---------------------------VALIDATE GET CATEGORY BY ID--------------------------------------------
def validate_get_category_by_id(params):
    category_id = int(params.get("category_id"))
    
    if not valid_int(category_id):
        return False, "category id is mandatory", None
    
    kwargs = {
        "category_id" :category_id,
    }
    return True, "validation successfully", kwargs
#---------------------------VALIDATE GET SUBCATEGORY BY ID--------------------------------------------
def validate_get_subcategory_by_id(params):
    subcategory_id = int(params.get("subcategory_id"))
    
    if not valid_int(subcategory_id):
        return False, "subcategory id is mandatory", None
    
    kwargs = {
        "subcategory_id" :subcategory_id,
    }
    return True, "validation successfully", kwargs
#---------------------------VALIDATE GET PRODUCT BY ID --------------------------------------------
def validate_get_product_by_id(params):
    product_id = int(params.get("product_id"))
    
    if not valid_int(product_id):
        return False, "product id is mandatory", None
    
    kwargs = {
        "product_id" :product_id,
    }
    return True, "validation successfully", kwargs
#---------------------------VALIDATE GET REGION COMPANY BY ID---------------------------------------
def validate_get_region_by_company_id(params):
    company_id = int(params.get("company_id"))
    
    if not valid_int(company_id):
        return False, "Company id is mandatory", None
    
    kwargs = {
        "company_id" :company_id,
    }
    return True, "validation successfully", kwargs
#---------------------------VALIDATE GET SUBREGION COMPANY BY ID---------------------------------------
def validate_get_subregion_by_company_id(params):
    company_id = int(params.get("company_id"))
    
    if not valid_int(company_id):
        return False, "Company id is mandatory", None
    
    kwargs = {
        "company_id" :company_id,
    }
    return True, "validation successfully", kwargs
#---------------------------VALIDATE GET CITY COMPANY BY ID---------------------------------------
def validate_get_city_by_company_id(params):
    company_id = int(params.get("company_id"))
    
    if not valid_int(company_id):
        return False, "Company id is mandatory", None
    
    kwargs = {
        "company_id" :company_id,
    }
    return True, "validation successfully", kwargs
#---------------------------VALIDATE GET STORE COMPANY BY ID---------------------------------------
def validate_get_store_by_company_id(params):
    company_id = int(params.get("company_id"))
    
    if not valid_int(company_id):
        return False, "Company id is mandatory", None
    
    kwargs = {
        "company_id" :company_id,
    }
    return True, "validation successfully", kwargs
#---------------------------VALIDATE UPDATE COMPANY---------------------------------------
def validate_update_company(params):
    company_id = int(params.get("company_id"))
    company_name = params.get("company_name")
    financial_start_date = params.get("financial_start_date")
    financial_end_date = params.get("financial_end_date")
    phone = params.get("phone")
    website = params.get("website")
    email = params.get("email")
    
    if not valid_int(company_id):
        return False, "Company id is mandatory", None
    if not valid_string(company_name):
        return False, "company name is mandatory", None
    if not valid_date_format(financial_start_date):
        return False, "Incorrect date format, should be YYYY-MM-DD", None
    if not valid_date_format(financial_end_date):
        return False, "Incorrect date format, should be YYYY-MM-DD", None
    if not valid_phone(phone):
        return False, "Please Enter Valid Phone Number", None
    if not valid_string(website):
        return False, "Website is mandatory", None
    if not valid_email(email):
        return False, "Please enter a proper email", None
    kwargs = {
        "company_id" : company_id,
        "company_name" : company_name,
        "financial_start_date" : financial_start_date,
        "financial_end_date" : financial_end_date,
        "phone" : phone,
        "website" : website,
        "email" : email
    }
    return True, "validation successfully", kwargs
#---------------------------VALIDATE UPDATE REGION---------------------------------------
def validate_update_region(params):
    company_id = params.get("company_id")
    region_name = params.get("region_name")
    region_id = params.get("region")

    if not valid_int(region_id):
        return False, "region id is mandatory", None
    if not valid_string(region_name):
        return False, "Region name is mandatory", None
    kwargs = {
        "region_id" :region_id,
        "region_name" :region_name
    }
    return True, "validation successfully", kwargs
#----------------------------VALIDATE UPDATE SUBREGION--------------------------------------
def validate_update_subregion(params):
    subregion_id = params.get("subregion_id")
    subregion_name = params.get("subregion_name")
    

    if not valid_int(subregion_id):
        return False, "subregion id is mandatory", None
    if not valid_string(subregion_name):
        return False, "Region name is mandatory", None
    kwargs = {
        "subregion_id" : subregion_id,
        "subregion_name" :subregion_name
    }
    return True, "validation successfully", kwargs
#----------------------------VALIDATE UPDATE CITY--------------------------------------
def validate_update_city(params):
    city_id = params.get("city_id")
    city_name = params.get("city_name")
    
    if not valid_int(city_id):
        return False, "city id is mandatory", None
    if not valid_string(city_name):
        return False, "City name is mandatory", None
    kwargs = {
        "city_id" : city_id,
        "city_name" :city_name
    }
    return True, "validation successfully", kwargs
#----------------------------VALIDATE UPDATE STORE--------------------------------------
def validate_update_store(request):
    try:
        params = request.POST
        store_id = int(params.get("store_id"))
        store_name = params.get("store_name")
        store_address = params.get("store_address")
        store_latitude = float(params.get("store_latitude"))
        store_longitude = float(params.get("store_longitude"))
        store_image = request.FILES.get("store_image")
        gstin = params.get("gstin")
        gstin_certificate = request.FILES.get("gstin_certificate")
        print("gstin_certificate", gstin_certificate)
        fssai = int(params.get("fssai"))
        fssai_certificate = request.FILES.get("fssai_certificate")
        print("fssai_certificate", fssai_certificate)
    
        if not valid_int(store_id):
            return False, "store id is mandatory", None
        if not valid_string(store_name):
            return False, "Store name is mandatory", None
        if not valid_string(store_address):
            return False, "Store address is mandatory", None
        if not valid_float(store_latitude):
            return False, "Store_latitude is mandatory", None
        if not valid_float(store_longitude):
            return False, "Store_longitude is mandatory", None
        if not valid_image_format(store_image):
            return False, "Upload Valid image file", None
        if not valid_gstin(gstin):
            return False, "Please enter Proper gstin number", None
        if not valid_csv_format(gstin_certificate):
            return False, "Upload Valid CSV file", None
        if not valid_fssai(fssai):
            return False, "Please enter Proper fssai number", None
        if not valid_csv_format(fssai_certificate):
            return False, "Upload Valid CSV file", None
        kwargs = {
            "store_id" : store_id,
            "store_name" :store_name,
            "store_address" : store_address,
            "store_latitude" : store_latitude,
            "store_longitude" : store_longitude,
            "store_image" : store_image,
            "gstin" : gstin,
            "gstin_certificate" : gstin_certificate,
            "fssai" : fssai,
            "fssai_certificate" : fssai_certificate,
        }
    except Exception as e:
        print(e)
        return False, str(e), None
    return True, "validation successfully", kwargs
#----------------------------VALIDATE UPDATE DEPARTMENT--------------------------------------
def validate_update_department(request):
    try:
        params = request.POST
        # store_id = int(params.get("store_id"))
        department_id = int(params.get("department_id"))
        department_name = params.get("department_name")
        department_image = request.FILES.get("department_image")
    
        if not valid_int(department_id):
            return False, "department id is mandatory", None
        if not valid_string(department_name):
            return False, "Department name is mandatory", None
        if not valid_image_format(department_image):
            return False, "Upload Valid image file", None
        kwargs = {
            "department_id" :department_id,
            "department_name" :department_name,
            "department_image" : department_image
        }
    except Exception as e:
        print(e)
        return False, str(e), None
    return True, "validation successfully", kwargs
#----------------------------VALIDATE UPDATE CATEGORY--------------------------------------
def validate_update_category(request):
    try:
        params = request.POST
        category_id = int(params.get("category_id"))
        category_name = params.get("category_name")
        category_image = request.FILES.get("category_image")
    
        if not valid_int(category_id):
            return False, "category id is mandatory", None
        if not valid_string(category_name):
            return False, "category name is mandatory", None
        if not valid_image_format(category_image):
            return False, "Upload Valid image file", None
        kwargs = {
            "category_id" : category_id,
            "category_name" :category_name,
            "category_image" : category_image
        }
    except Exception as e:
        print(e)
        return False, str(e), None
    return True, "validation successfully", kwargs
#----------------------------VALIDATE UPDATE SUBCATEGORY--------------------------------------
def validate_update_subcategory(request):
    try:
        params = request.POST
        # store_id = params.get("store_id")
        # category_id = params.get("category_id")
        subcategory_id = int(params.get("subcategory_id"))
        subcategory_name = params.get("subcategory_name")
        subcategory_image = request.FILES.get("subcategory_image")

        if not valid_int(subcategory_id):
            return False, "category id is mandatory", None
        if not valid_string(subcategory_name):
            return False, "subcategory name is mandatory", None
        if not valid_image_format(subcategory_image):
            return False, "Upload Valid image file", None
        kwargs = {
            # "category_id" : category_id,
            "subcategory_id" : subcategory_id,
            "subcategory_name" :subcategory_name,
            "subcategory_image" : subcategory_image
        }
    except Exception as e:
        print(e)
        return False, str(e), None
    return True, "validation successfully", kwargs
#----------------------------VALIDATE UPDATE PRODUCT--------------------------------------
def validate_update_product(request):
    try:
        params = request.POST
        product_id = int(params.get("product_id"))
        product_name = params.get("product_name")
        product_price = float(params.get("product_price"))
        product_discount_price = float(params.get("product_discount_price"))
        product_quantity = int(params.get("product_quantity"))
        product_description = params.get("product_description")
        product_image = request.FILES.get("product_image")
        
        if not valid_int(product_id):
            return False, "product id is mandatory", None
        if not valid_string(product_name):
            return False, "product name is mandatory", None
        if not valid_float(product_price):
            return False, "product_price is mandatory", None
        if not valid_float(product_discount_price):
            return False, "product_discount_price is mandatory", None
        if not valid_int(product_quantity):
            return False, "Product quantity is mandatory", None
        if not valid_string(product_description):
            return False, "product_description is mandatory", None
        if not valid_image_format(product_image):
            return False, "Upload Valid image file", None
        kwargs = {
            "product_id" : product_id,
            "product_name" :product_name,
            "product_price" : product_price,
            "product_discount_price" : product_discount_price,
            "product_quantity" : product_quantity,
            "product_description" : product_description,
            "product_image" : product_image
        }
    except Exception as e:
        print(e)
        return False, str(e), None
    return True, "validation successfully", kwargs

def validate_add_follower_to_the_store(params):
    try:
        store_id = int(params.get("store_id"))
        user_profile_id = int(params.get("user_profile_id"))
        if not valid_int(store_id):
            return False, "store id is mandatory", None
        if not valid_int(user_profile_id):
            return False, "user profile id is mandatory", None
         
        kwargs = {
            "store_id" : store_id,
            "user_profile_id" : user_profile_id
        }
    except Exception as e:
        print(e)
        return False, str(e), None
    return True, "validation successfully", kwargs

def validate_remove_follower_from_store(params):
    try:
        store_id = int(params.get("store_id"))
        user_profile_id = int(params.get("user_profile_id"))
        remove_reason = params.get("remove_reason")
        
        if not valid_int(store_id):
            return False, "store id is mandatory", None  
        if not valid_int(user_profile_id):
            return False, "user profile id is mandatory", None  
        if not valid_string(remove_reason):
            return False, "remove reason id is mandatory", None
        
        kwargs = {
            "store_id" : store_id,
            "user_profile_id" : user_profile_id,
            "remove_reason" : remove_reason
        }
    except Exception as e:
        print(e)
        return False, str(e), None
    return True, "validation successfully", kwargs