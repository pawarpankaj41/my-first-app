from django.shortcuts import render
from .models import Company, Region, SubRegion, Store, Department, Category, Subcategory, Product, Followership
from django.http import HttpResponse, JsonResponse
import json
from django.db import transaction
import os
from django.core.exceptions import ObjectDoesNotExist
from newuser.models import UserProfile
from .validations import *
from .helpers import *
from newuser.validations import validate_userprofile_id
# Create your views here.

#--------------------------------CREATE COMPANY------------------------------------------------
def create_company(request):
    try:
        params = json.loads(request.body)
        print("params $$$$$$$$$", params)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_create_company(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    company_data, status = create_company_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------CREATE REGION----------------------------------------------
def create_region(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_create_region(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    region_data, status = create_region_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------CREATE SUBREGION----------------------------------------------
def create_subregion(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_create_subregion(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    subregion_data, status = create_subregion_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------CREATE CITY----------------------------------------------
def create_city(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_create_city(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    city_data, status = create_city_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------CREATE STORE----------------------------------------------
def create_store(request):
    status, message, data = validate_create_store(request)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    store_data, status = create_store_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True })
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------CREATE DEPARTMENT----------------------------------------------
def create_department(request):
    status, message, data = validate_create_department(request)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    department_data, status = create_department_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------CREATE CATEGORY----------------------------------------------
def create_category(request):
    status, message, data = validate_create_category(request)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    category_data, status = create_category_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------CREATE SUBCATEGORY----------------------------------------------
def create_subcategory(request):
    status, message, data = validate_create_subcategory(request)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    subcategory_data, status = create_subcategory_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------CREATE PRODUCT----------------------------------------------
def create_product(request):
    status, message, data = validate_create_product(request)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    product_data, status = create_product_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------GET COMPANY BY ID------------------------------------------
def get_company_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_company_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    company_data, status, message = get_company_by_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : company_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET REGION BY ID------------------------------------------
def get_region_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_region_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    region_data, status, message = get_region_by_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : region_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET SUBREGION BY ID------------------------------------------
def get_subregion_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_subregion_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    subregion_data, status, message = get_subregion_by_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : subregion_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET CITY BY ID------------------------------------------
def get_city_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_city_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    city_data, status, message = get_city_by_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : city_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET STORE BY ID----------------------------------------------
def get_store_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_store_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    store_data, status, message = get_store_by_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : store_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET DEPARTMENT BY ID------------------------------------------
def get_department_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_department_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    department_data, status, message = get_department_by_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : department_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET CATEGORY BY ID------------------------------------------
def get_category_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_category_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    category_data, status, message = get_category_by_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : category_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET SUBCATEGORY BY ID------------------------------------------
def get_subcategory_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_subcategory_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    subcategory_data, status, message = get_subcategory_by_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : subcategory_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET PRODUCT BY ID------------------------------------------
def get_product_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_product_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    product_data, status, message = get_product_by_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : product_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET ALL COMPANY-----------------------------------------
def get_all_company(request):
    company_data, status, message = get_all_company_function()
    if status:
        return JsonResponse({'validation' : message, "data" : company_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET ALL REGION-----------------------------------------
def get_all_region(request):
    region_data, status, message = get_all_region_function()
    if status:
        return JsonResponse({'validation' : message, "data" : region_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET ALL SUBREGION-----------------------------------------
def get_all_subregion(request):
    subregion_data, status, message = get_all_subregion_function()
    if status:
        return JsonResponse({'validation' : message, "data" : subregion_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET ALL CITY-----------------------------------------
def get_all_city(request):
    city_data, status, message = get_all_city_function()
    if status:
        return JsonResponse({'validation' : message, "data" : city_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET ALL STORE-----------------------------------------
def get_all_store(request):
    store_data, status, message = get_all_store_function()
    if status:
        return JsonResponse({'validation' : message, "data" : store_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET ALL DEPARTMENT-----------------------------------------
def get_all_department(request):
    department_data, status, message = get_all_department_function()
    if status:
        return JsonResponse({'validation' : message, "data" : department_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET ALL CATEGORY-----------------------------------------
def get_all_category(request):
    category_data, status, message = get_all_category_function()
    if status:
        return JsonResponse({'validation' : message, "data" : category_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET ALL SUBCATEGORY-----------------------------------------
def get_all_subcategory(request):
    subcategory_data, status, message = get_all_subcategory_function()
    if status:
        return JsonResponse({'validation' : message, "data" : subcategory_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET ALL PRODUCT-----------------------------------------
def get_all_product(request):
    product_data, status, message = get_all_product_function()
    if status:
        return JsonResponse({'validation' : message, "data" : product_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET REGION BY COMPANY ID----------------------------------
def get_region_by_company_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_region_by_company_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    region_data, status, message = get_region_by_company_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : region_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET SUBREGION BY COMPANY ID------------------------------
def get_subregion_by_company_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_subregion_by_company_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    subregion_data, status, message = get_subregion_by_company_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : subregion_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET CITY BY COMPANY ID------------------------------
def get_city_by_company_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_city_by_company_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    city_data, status, message = get_city_by_company_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : city_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET STORE BY COMPANY ID------------------------------
def get_store_by_company_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_store_by_company_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    store_data, status, message = get_store_by_company_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : store_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------UPDATE COMPANY-----------------------------------------
def update_company_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_update_company(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    company_data, status = update_company_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------UPDATE REGION-----------------------------------------
def update_region_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_update_region(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    region_data, status = update_region_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------UPDATE SUBREGION-----------------------------------------
def update_subregion_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_update_subregion(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    subregion_data, status = update_subregion_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------UPDATE CITY-----------------------------------------
def update_city_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_update_city(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    city_data, status = update_city_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------UPDATE STORE-----------------------------------------
def update_store_by_id(request):
    status, message, data = validate_update_store(request)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    store_data, status = update_store_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------UPDATE department-----------------------------------------
def update_department_by_id(request):
    status, message, data = validate_update_department(request)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    department_data, status = update_department_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------UPDATE category-----------------------------------------
def update_category_by_id(request):
    status, message, data = validate_update_category(request)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    category_data, status = update_category_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------UPDATE subcategory-----------------------------------------
def update_subcategory_by_id(request):
    status, message, data = validate_update_subcategory(request)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    subcategory_data, status = update_subcategory_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------UPDATE product-----------------------------------------
def update_product_by_id(request):
    status, message, data = validate_update_product(request)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    product_data, status = update_product_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------DELETE COMPANY-----------------------------------------
def delete_company_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_company_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    try:
        Company.objects.get(id = data["company_id"]).delete()
        return JsonResponse({"validation": "success", "status": True})
    except ObjectDoesNotExist :
        return JsonResponse({"validation": "invalid id", "status" : False})
    except Exception as e:
        return JsonResponse({"validation" : str(e), "status" : False})
#----------------------------------DELETE REGION-----------------------------------------
def delete_region_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_region_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    try:
        Region.objects.get(id = data["region_id"]).delete()
        return JsonResponse({"validation": "success", "status": True})
    except ObjectDoesNotExist :
        return JsonResponse({"validation": "invalid id", "status" : False})
    except Exception as e:
        return JsonResponse({"validation" : str(e), "status" : False})
#----------------------------------DELETE SUBREGION-----------------------------------------
def delete_subregion_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_subregion_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    try:
        SubRegion.objects.get(id = data["subregion_id"]).delete()
        return JsonResponse({"validation": "success", "status": True})
    except ObjectDoesNotExist :
        return JsonResponse({"validation": "invalid id", "status" : False})
    except Exception as e:
        return JsonResponse({"validation" : str(e), "status" : False})
#----------------------------------DELETE CITY-----------------------------------------
def delete_city_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_city_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    try:
        City.objects.get(id = data["city_id"]).delete()
        return JsonResponse({"validation": "success", "status": True})
    except ObjectDoesNotExist :
        return JsonResponse({"validation": "invalid id", "status" : False})
    except Exception as e:
        return JsonResponse({"validation" : str(e), "status" : False})
#----------------------------------DELETE STORE-----------------------------------------
def delete_store_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_store_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    try:
        Store.objects.get(id = data["store_id"]).delete()
        return JsonResponse({"validation": "success", "status": True})
    except ObjectDoesNotExist :
        return JsonResponse({"validation": "invalid id", "status" : False})
    except Exception as e:
        return JsonResponse({"validation" : str(e), "status" : False})
#----------------------------------DELETE DEPARTMENT-----------------------------------------
def delete_department_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_department_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    try:
        Department.objects.get(id = data["department_id"]).delete()
        return JsonResponse({"validation": "success", "status": True})
    except ObjectDoesNotExist :
        return JsonResponse({"validation": "invalid id", "status" : False})
    except Exception as e:
        return JsonResponse({"validation" : str(e), "status" : False})
#----------------------------------DELETE CATEGORY-----------------------------------------
def delete_category_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_category_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    try:
        Category.objects.get(id = data["category_id"]).delete()
        return JsonResponse({"validation": "success", "status": True})
    except ObjectDoesNotExist :
        return JsonResponse({"validation": "invalid id", "status" : False})
    except Exception as e:
        return JsonResponse({"validation" : str(e), "status" : False})
#----------------------------------DELETE SUBCATEGORY-----------------------------------------
def delete_subcategory_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_subcategory_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    try:
        Subcategory.objects.get(id = data["subcategory_id"]).delete()
        return JsonResponse({"validation": "success", "status": True})
    except ObjectDoesNotExist :
        return JsonResponse({"validation": "invalid id", "status" : False})
    except Exception as e:
        return JsonResponse({"validation" : str(e), "status" : False})
#----------------------------------DELETE PRODUCT-----------------------------------------
def delete_product_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_product_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    try:
        Product.objects.get(id = data["product_id"]).delete()
        return JsonResponse({"validation": "success", "status": True})
    except ObjectDoesNotExist :
        return JsonResponse({"validation": "invalid id", "status" : False})
    except Exception as e:
        return JsonResponse({"validation" : str(e), "status" : False})
#----------------------------------GET DEPARTMENT BY STORE ID-------------------------------
def get_department_by_store_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_store_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    department_data, status, message = get_department_by_store_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : department_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET CATEGORY BY STORE ID-------------------------------
def get_category_by_store_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_store_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    category_data, status, message = get_category_by_store_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : category_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET SUBCATEGORY BY STORE ID-------------------------------  
def get_subcategory_by_store_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_store_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    subcategory_data, status, message = get_subcategory_by_store_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : subcategory_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET PRODUCT BY STORE ID-------------------------------
def get_product_by_store_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_store_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    product_data, status, message = get_product_by_store_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : product_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET CATEGORY BY DEPARTMENT ID-------------------------------
def get_category_by_department_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_department_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    category_data, status, message = get_category_by_store_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : category_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET SUBCATEGORY BY CATEGORY ID-------------------------------
def get_subcategory_by_category_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_category_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    subcategory_data, status, message = get_subcategory_by_store_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : subcategory_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------GET PRODUCT BY SUBCATEGORY ID-------------------------------
def get_product_by_subcategory_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_subcategory_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    product_data, status, message = get_product_by_store_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : product_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})
#----------------------------------ADD FOLLOWER TO THE STORE-------------------------------
def add_follower_to_the_store(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_add_follower_to_the_store(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    follower_data, status, message = add_follower_to_the_store_function(data)
    # print(follower_data)
    if status:
        return JsonResponse({'validation' : message, "data" : follower_data.get_json()})
    else:
        return JsonResponse({'validation' : message, "status" : False})

def get_followers_by_store(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_get_store_by_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    product_data, status, message = get_follower_by_stores_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : product_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})

def get_stores_by_follower(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_userprofile_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    store_data, status, message = get_stores_by_follower_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : store_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})

def remove_follower_from_the_store(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_remove_follower_from_store(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    store_data, status, message = remove_follower_from_the_store_function(data)
    
    if status:
        return JsonResponse({'validation' : message, "status" : True})
    else:
        return JsonResponse({'validation' : message, "status" : False})
    
    






# def department_update_or_create_by_id(request):
#     params = request.POST
#     department_id = params.get('department_id')
#     store_id = params.get("store_id")
#     store = Store.objects.get(id = store_id)
#     department_name = params.get("department_name")
#     department_image = request.FILES.get('department_image')
#     try:
#         department = Department.objects.update_or_create(id = department_id,
#         defaults = {
#             "store" : store,
#             "department_name" : department_name,
#             "department_image" : department_image
#         }
       
#         )
#         return JsonResponse({"validation": "success", "status": True})
#     except ObjectDoesNotExist :
#         return JsonResponse({"validation": "invalid id", "status" : False})
#     except Exception as e:
#         return JsonResponse({"validation" : str(e), "status" : False})
