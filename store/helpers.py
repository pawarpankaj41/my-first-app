from django.shortcuts import render
from .models import Company, Region, SubRegion, City, Store, Department, Category, Subcategory, Product, Followership
from django.http import HttpResponse, JsonResponse
from django.db import transaction
import json
import os
from newuser.models import UserProfile
from django.core.exceptions import ObjectDoesNotExist

#---------------------------CREATE COMPANY FUNCTION-----------------------------------------
def create_company_function(data):
    try:
        with transaction.atomic():
            customer_data = Company.objects.create(
                company_name = data["company_name"],
                financial_start_date = data["financial_start_date"],
                financial_end_date = data["financial_end_date"],
                phone = data["phone"],
                website = data["website"],
                email = data["email"]
            )
        return {"customer data": customer_data}, True
    except Exception as e:
        print(e)
        return None, False
#-----------------------------CREATE REGION FUNCTION---------------------------------------
def create_region_function(data):
    company = Company.objects.get(id = data["company_id"])
    try:
        with transaction.atomic():
            region_data = Region.objects.create(
                company = company,
                region_name = data["region_name"]
            )
        return {"reigon_data": region_data}, True
    except Exception as e:
        print(e)
        return None, False
#-----------------------------CREATE SUBREGION FUNCTION---------------------------------------
def create_subregion_function(data):
    company = Company.objects.get(id = data["company_id"])
    region = Region.objects.get(id = data["region_id"])
    try:
        with transaction.atomic():
            subregion_data = SubRegion.objects.create(
                company = company,
                region = region,
                subregion_name = data["subregion_name"]
            )
        return {"subreigon_data": subregion_data}, True
    except Exception as e:
        print(e)
        return None, False
#-----------------------------CREATE CITY FUNCTION---------------------------------------
def create_city_function(data):
    company = Company.objects.get(id = data["company_id"])
    if data["subregion_id"] is not None:
        subregion = SubRegion.objects.get(id = data["subregion_id"])
    try:
        with transaction.atomic():
            city_data = City.objects.create(
                company = company,
                subregion = subregion,
                city_name = data["city_name"]
            )
        return {"city_data": city_data}, True
    except Exception as e:
        print(e)
        return None, False
#-----------------------------CREATE STORE FUNCTION---------------------------------------
def create_store_function(data):
    company = Company.objects.get(id = data["company_id"])
    city = City.objects.get(id = data["city_id"])
    try:
        with transaction.atomic():
            store_data = Store.objects.create(
                company = company,
                city = city,
                store_name = data["store_name"],
                store_address = data["store_address"],
                store_latitude = data["store_latitude"],
                store_longitude = data["store_longitude"],
                store_image = data["store_image"],
                gstin = data["gstin"],
                gstin_certificate = data["gstin_certificate"],
                fssai = data["fssai"],
                fssai_certificate = data["fssai_certificate"]
            )
        return {"store_data": store_data}, True
    except Exception as e:
        print(e)
        return None, False
#-----------------------------CREATE DEPARTMENT FUNCTION---------------------------------------
def create_department_function(data):
    store = Store.objects.get(id = data["store_id"])
    try:
        with transaction.atomic():
            department_data = Department.objects.create(
                store = store,
                department_name = data["department_name"],
                department_image = data["department_image"]
            )
        return {"department_data": department_data}, True
    except Exception as e:
        print(e)
        return None, False
#-----------------------------CREATE CATEGORY FUNCTION---------------------------------------
def create_category_function(data):
    store = Store.objects.get(id = data["store_id"])
    department = Department.objects.get(id = data["department_id"])
    try:
        with transaction.atomic():
            category_data = Category.objects.create(
                store = store,
                department = department,
                category_name = data["category_name"],
                category_image = data["category_image"]
            )
        return {"category_data": category_data}, True
    except Exception as e:
        print(e)
        return None, False
#-----------------------------CREATE SUBCATEGORY FUNCTION---------------------------------------
def create_subcategory_function(data):
    store = Store.objects.get(id = data["store_id"])
    category = Category.objects.get(id = data["category_id"])
    try:
        with transaction.atomic():
            subcategory_data = Subcategory.objects.create(
                store = store,
                category = category,
                subcategory_name = data["subcategory_name"],
                subcategory_image = data["subcategory_image"]
            )
        return {"subcategory_data": subcategory_data}, True
    except Exception as e:
        print(e)
        return None, False
#-----------------------------CREATE PRODUCT FUNCTION---------------------------------------
def create_product_function(data):
    store = Store.objects.get(id = data["store_id"])
    subcategory = Subcategory.objects.get(id = data["subcategory_id"])
    try:
        with transaction.atomic():
            product_data = Product.objects.create(
                store = store,
                subcategory = subcategory,
                product_name = data["product_name"],
                product_price = data["product_price"],
                product_discount_price = data["product_discount_price"],
                product_quantity = data["product_quantity"],
                product_description = data["product_description"],
                product_image = data["product_image"]
            )
        return {"product_data": product_data}, True
    except Exception as e:
        print(e)
        return None, False
#-----------------------------GET COMPANY BY ID FUNCTION---------------------------------------
def get_company_by_id_function(data):
    try:
        company_data = Company.objects.get(id = data["company_id"])
        data = company_data.get_json()
        return data, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)
#-----------------------------GET REGION BY ID FUNCTION---------------------------------------
def get_region_by_id_function(data):
    try:
        region_data = Region.objects.get(id = data["region_id"])
        data = region_data.get_json()
        return data, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)
#-----------------------------GET SUBREGION BY ID FUNCTION---------------------------------------
def get_subregion_by_id_function(data):
    try:
        subregion_data = SubRegion.objects.get(id = data["subregion_id"])
        data = subregion_data.get_json()
        return data, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)
#-----------------------------GET CITY BY ID FUNCTION---------------------------------------
def get_city_by_id_function(data):
    try:
        city_data = City.objects.get(id = data["city_id"])
        data = city_data.get_json()
        return data, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)
#-----------------------------GET STORE BY ID FUNCTION---------------------------------------
def get_store_by_id_function(data):
    try:
        store_data = Store.objects.get(id = data["store_id"])
        data = store_data.get_json()
        print(data)
        return data, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)
#-----------------------------GET DEPARTMENT BY ID FUNCTION---------------------------------------
def get_department_by_id_function(data):
    try:
        department_data = Department.objects.get(id = data["department_id"])
        data = department_data.get_json()
        return data, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)
#-----------------------------GET CATEGORY BY ID FUNCTION---------------------------------------
def get_category_by_id_function(data):
    try:
        category_data = Category.objects.get(id = data["category_id"])
        data = category_data.get_json()
        return data, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)
#-----------------------------GET SUBCATEGORY BY ID FUNCTION---------------------------------------
def get_subcategory_by_id_function(data):
    try:
        subcategory_data = Subcategory.objects.get(id = data["subcategory_id"])
        data = subcategory_data.get_json()
        return data, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)
#-----------------------------GET PRODUCT BY ID FUNCTION---------------------------------------
def get_product_by_id_function(data):
    try:
        product_data = Product.objects.get(id = data["product_id"])
        data = product_data.get_json()
        return data, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)
#----------------------------------GET ALL COMPANY FUNCTION------------------------------------------
def get_all_company_function():
    data = []
    try:
        company_data = Company.objects.all()
        for obj in company_data:   
            data.append(obj.get_json())
        return data, True, "Successful"
    except Exception as e:
        print(e)
        return None, False, str(e)
#----------------------------------GET ALL REGION FUNCTION---------------------------------------
def get_all_region_function():
    data = []
    try:
        region_data = Region.objects.all()
        for obj in region_data:   
            data.append(obj.get_json())
        return data, True, "Successful"
    except Exception as e:
        print(e)
        return None, False, str(e)
#----------------------------------GET ALL SUBREGION FUNCTION--------------------------------------
def get_all_subregion_function():
    data = []
    try:
        subregion_data = SubRegion.objects.all()
        for obj in subregion_data:   
            data.append(obj.get_json())
        return data, True, "Successful"
    except Exception as e:
        print(e)
        return None, False, str(e)
#----------------------------------GET ALL CITY FUNCTION--------------------------------------
def get_all_city_function():
    data = []
    try:
        city_data = City.objects.all()
        for obj in city_data:   
            data.append(obj.get_json())
        return data, True, "Successful"
    except Exception as e:
        print(e)
        return None, False, str(e)
#----------------------------------GET ALL STORE FUNCTION--------------------------------------
def get_all_store_function():
    data = []
    try:
        store_data = Store.objects.all()
        for obj in store_data:   
            data.append(obj.get_json())
        return data, True, "Successful"
    except Exception as e:
        print(e)
        return None, False, str(e)
#----------------------------------GET ALL DEPARTMENT FUNCTION--------------------------------------
def get_all_department_function():
    data = []
    try:
        department_data = Department.objects.all()
        for obj in department_data:   
            data.append(obj.get_json())
        return data, True, "Successful"
    except Exception as e:
        print(e)
        return None, False, str(e)
#----------------------------------GET ALL CATEGORY FUNCTION--------------------------------------
def get_all_category_function():
    data = []
    try:
        category_data = Category.objects.all()
        for obj in category_data:   
            data.append(obj.get_json())
        return data, True, "Successful"
    except Exception as e:
        print(e)
        return None, False, str(e)
#----------------------------------GET ALL SUBCATEGORY FUNCTION--------------------------------------
def get_all_subcategory_function():
    data = []
    try:
        subcategory_data = Subcategory.objects.all()
        for obj in subcategory_data:   
            data.append(obj.get_json())
        return data, True, "Successful"
    except Exception as e:
        print(e)
        return None, False, str(e)
#----------------------------------GET ALL PRODUCT FUNCTION--------------------------------------
def get_all_product_function():
    data = []
    try:
        product_data = Product.objects.all()
        for obj in product_data:   
            data.append(obj.get_json())
        return data, True, "Successful"
    except Exception as e:
        print(e)
        return None, False, str(e)
#---------------------------GET REGION COMPANY ID FUNCTION----------------------------------
def get_region_by_company_id_function(data):
    try:
        region_data = Region.objects.get(id = data["company_id"])
        data = region_data.get_json()
        return data, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)
#---------------------------GET SUBREGION COMPANY ID FUNCTION----------------------------------
def get_subregion_by_company_id_function(data):
    try:
        subregion_data = SubRegion.objects.get(id = data["company_id"])
        data = subregion_data.get_json()
        return data, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)
#---------------------------GET CITY COMPANY ID FUNCTION----------------------------------
def get_city_by_company_id_function(data):
    try:
        city_data = City.objects.get(id = data["company_id"])
        data = city_data.get_json()
        return data, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)
#---------------------------GET STORE COMPANY ID FUNCTION----------------------------------
def get_store_by_company_id_function(data):
    try:
        store_data = Store.objects.get(id = data["company_id"])
        data = store_data.get_json()
        return data, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)
#---------------------------UPDATE COMPANY FUNCTION-----------------------------------------
def update_company_function(data):
    try:
        with transaction.atomic():
            company_data = Company.objects.get(id=data["company_id"])
            company_data.company_name = data["company_name"]
            company_data.financial_start_date = data["financial_start_date"]
            company_data.financial_end_date = data["financial_end_date"]
            company_data.phone = data["phone"]
            company_data.website = data["website"]
            company_data.email = data["email"]
            company_data.save()
        return {"company data": company_data}, True
    except Exception as e:
        print(e)
        return None, False
#---------------------------UPDATE REGION FUNCTION-----------------------------------------
def update_region_function(data):
    try:
        with transaction.atomic():
            region_data = Region.objects.get(id=data["region_id"])
            region_data.region_name = data["region_name"]
            region_data.save()
        return {"region data": region_data}, True
    except Exception as e:
        print(e)
        return None, False
#---------------------------UPDATE SUBREGION FUNCTION-----------------------------------------
def update_subregion_function(data):
    try:
        with transaction.atomic():
            subregion_data = SubRegion.objects.get(id=data["subregion_id"])
            subregion_data.subregion_name = data["subregion_name"]
            subregion_data.save()
        return {"subregion data": subregion_data}, True
    except Exception as e:
        print(e)
        return None, False
#---------------------------UPDATE CITY FUNCTION-----------------------------------------
def update_city_function(data):
    try:
        with transaction.atomic():
            city_data = City.objects.get(id=data["city_id"])
            city_data.city_name = data["city_name"]
            city_data.save()
        return {"city data": city_data}, True
    except Exception as e:
        print(e)
        return None, False
#---------------------------UPDATE STORE FUNCTION-----------------------------------------
def update_store_function(data):
    try:
        with transaction.atomic():
            store_data = Store.objects.get(id=data["store_id"])
            store_data.store_name = data["store_name"]
            store_data.store_address = data['store_address']
            store_data.store_latitude = data['store_latitude']
            store_data.store_longitude = data['store_longitude']
            store_data.store_image = data['store_image']
            store_data.save()
        return {"store data": store_data}, True
    except Exception as e:
        print(e)
        return None, False
#---------------------------UPDATE DEPARTMENT FUNCTION-----------------------------------------
def update_department_function(data):
    try:
        with transaction.atomic():
            department_data = Department.objects.get(id=data["department_id"])
            department_data.department_name = data["department_name"]
            department_data.department_image = data['department_image']
            department_data.save()
        return {"department data": department_data}, True
    except Exception as e:
        print(e)
        return None, False
#---------------------------UPDATE CATEGORY FUNCTION-----------------------------------------
def update_category_function(data):
    try:
        with transaction.atomic():
            category_data = Category.objects.get(id=data["category_id"])
            category_data.category_name = data["category_name"]
            category_data.category_image = data['category_image']
            category_data.save()
        return {"category data": category_data}, True
    except Exception as e:
        print(e)
        return None, False
#---------------------------UPDATE SUBCATEGORY FUNCTION-----------------------------------------
def update_subcategory_function(data):
    try:
        with transaction.atomic():
            subcategory_data = Subcategory.objects.get(id=data["subcategory_id"])
            subcategory_data.subcategory_name = data["subcategory_name"]
            subcategory_data.subcategory_image = data['subcategory_image']
            subcategory_data.save()
        return {"subcategory data": subcategory_data}, True
    except Exception as e:
        print(e)
        return None, False
#---------------------------UPDATE PRODUCT FUNCTION-----------------------------------------
def update_product_function(data):

    try:
        with transaction.atomic():
            product_data = Product.objects.get(id=data["product_id"])
            product_data.product_name = data["product_name"]
            product_data.product_price = data["product_price"]
            product_data.product_discount_price = data["product_discount_price"]
            product_data.product_quantity = data["product_quantity"]
            product_data.product_description = data["product_description"]
            product_data.product_image = data['product_image']
            product_data.save()
        return {"product data": product_data}, True
    except Exception as e:
        print(e)
        return None, False

def get_department_by_store_id_function(data):
    try:
        response = []
        store_detail = Store.objects.get(id = data["store_id"])
        department_data = Department.objects.get(store = store_detail)
        for obj in department_data:
            response.append(department_data.get_json())
        return response, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)

def get_category_by_store_id_function(data):
    try:
        response = []
        store_detail = Store.objects.get(id = data["store_id"])
        category_data = Category.objects.get(store = store_detail)
        for obj in category_data:
            response.append(category_data.get_json())
        return response, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)

def get_subcategory_by_store_id_function(data):
    try:
        response = []
        store_detail = Store.objects.get(id = data["store_id"])
        subcategory_data = Subcategory.objects.get(store = store_detail)
        for obj in subcategory_data:
            response.append(subcategory_data.get_json())
        return response, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)

def get_product_by_store_id_function(data):
    try:
        response = []
        store_detail = Store.objects.get(id = data["store_id"])
        product_data = Product.objects.get(store = store_detail)
        for obj in product_data:
            response.append(product_data.get_json())
        return response, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)

def get_category_by_department_id_function(data):
    try:
        response = []
        department_detail = Department.objects.get(id = data["department_id"])
        category_data = Category.objects.get(department = department_detail)
        for obj in category_data:
            response.append(category_data.get_json())
        return response, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)

def get_subcategory_by_category_id_function(data):
    try:
        response = []
        category_detail = Category.objects.get(id = data["category_id"])
        subcategory_data = Subcategory.objects.get(category = category_detail)
        for obj in subcategory_data:
            response.append(subcategory_data.get_json())
        return response, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)

def get_product_by_subcategory_id_function(data):
    try:
        response = []
        department_detail = Department.objects.get(id = data["department_id"])
        product_data = Product.objects.get(department = department_detail)
        for obj in product_data:
            response.append(product_data.get_json())
        return response, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)

def add_follower_to_the_store_function(data):
    try:
        store_obj = Store.objects.get(id = data["store_id"])
        store_obj.followers.add(data["user_profile_id"])
        store_obj.save()
        return store_obj, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)

def get_follower_by_stores_function(data):
    try:
        StoreObj = Store.objects.get(id = data["store_id"])
        data = StoreObj.get_followers()
        return data, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)
def get_stores_by_follower_function(data):
    try:
        response = []
        followerObj = UserProfile.objects.get(id = data["user_profile_id"])
        storesobj = Store.objects.filter(followers = followerObj)
        for obj in storesobj:
            response.append(obj.get_json())
        return response, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)

def remove_follower_from_the_store_function(data):
    try:
        storeObj = Store.objects.get(id = data["store_id"])
        userobj = UserProfile.objects.get(id = data["user_profile_id"])
        followerObj = Followership.objects.filter(store = storeObj)
       
        print("followerObj", followerObj)
        obj = followerObj.get(users = userobj)
        print("obj", obj)
        obj.users = None
        obj.remove_reason = data["remove_reason"]
        obj.save()
        return obj, True, "Successful"
    except ObjectDoesNotExist:
        return None, False, "Invalid Id"
    except Exception as e:
        print(e)
        return None, False, str(e)
