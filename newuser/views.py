from django.shortcuts import render
import json
from .models import *
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.db import transaction
from django.contrib.auth import get_user_model, logout
from .validations import *
from .helpers import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.conf import settings
from django.core.mail import send_mail

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def email(request):
    subject = 'New Product in our Store'
    message = 'This new product is added in our store'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = []
    send_mail( subject, message, email_from, recipient_list )
    

def login_view(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_login(params)
    if not status:
        return JsonResponse({"validation": str(e), "status": False })
    user_data, status = login_function(request, data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "stat" : False})

def logout_view(request):
    try:
        logout(request)
        return JsonResponse({'validation message' : "successful", "status" : True})
    except Exception as e:
        return JsonResponse({'validation message' : str(e), "stat" : False})
 
def change_password_view(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_change_password(params)
    print(data)
    if not status:
        return JsonResponse({"validation": "unsuccessful", "status": False })
    user_data, status = change_password_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "stat" : False})

def forget_password_view(request):
    try:
        params = json.loads(request.body)
        print(params)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_forget_password(params)
    print(data, message, status)
    if not status:
        return JsonResponse({"validation": "unsuccessful", "status": False })
    user_data, status = forget_password_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "stat" : False})





def create_user_profile(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_create_user_profile(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    user_profile_data, status = create_user_profile_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})
#----------------------------------CREATE REGION--------------------------
def create_address(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_create_address(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    address_data, status = create_address_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})

def create_buyersprofile(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_userprofile_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    buyersprofile_data, status = create_buyersprofile_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})

def create_sellersprofile(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_create_sellersprofile(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    sellersprofile_data, status = create_sellersprofile_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})

def get_user_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_userprofile_id(params)
    print(data)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    user_data, status, message = get_user_by_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : user_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})

def get_address_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_userprofile_id(params)
    print(data)
    print(type(data))
    if not status:
        return JsonResponse({"validation": message, "status": False })
    address_data, status, message = get_address_by_userprofile_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : address_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})

def get_buyersprofile_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_buyersprofile_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    buyersprofile_data, status, message = get_buyersprofile_by_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : buyersprofile_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})

def get_sellersprofile_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_sellersprofile_id(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    sellersprofile_data, status, message = get_sellersprofile_by_id_function(data)
    if status:
        return JsonResponse({'validation' : message, "data" : sellersprofile_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})

def get_all_userprofile(request):
    userprofile_data, status, message = get_all_userprofile_function()
    if status:
        return JsonResponse({'validation' : message, "data" : userprofile_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})

def get_all_buyersprofile(request):
    buyersprofile_data, status, message = get_all_buyersprofile_function()
    if status:
        return JsonResponse({'validation' : message, "data" : buyersprofile_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})

def get_all_sellersprofile(request):
    sellersprofile_data, status, message = get_all_sellersprofile_function()
    if status:
        return JsonResponse({'validation' : message, "data" : sellersprofile_data})
    else:
        return JsonResponse({'validation' : message, "status" : False})

def update_userprofile_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_update_user_profile(params)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    userprofile_data, status = update_userprofile_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})


def update_address_by_id(request):
    try:
        params = json.loads(request.body)
    except Exception as e:
        print(e)
        return JsonResponse({"validation" : str(e), "status" : False})
    status, message, data = validate_update_address(params)
    print(data)
    if not status:
        return JsonResponse({"validation": message, "status": False })
    address_data, status = update_address_function(data)
    if status:
        return JsonResponse({'validation message' : "successful", "status" : True})
    else:
        return JsonResponse({'validation message' : "unsuccessful", "status" : False})

# def filter_by_first_name(request):
#     params = json.loads(request.body)
#     firstname = params.get("first_name")
#     lastname = params.get("last_name")

#     response = []
#     userprofile = ()
#     if firstname and lastname:
#         userprofile = UserProfile.objects.filter(first_name__startswith = firstname,last_name__startswith = lastname)
#     if firstname:
#         userprofile = UserProfile.objects.filter(first_name__startswith = firstname)
#     if lastname:
#         userprofile = UserProfile.objects.filter(last_name__startswith = lastname)
    
#     #userprofile = UserProfile.objects.filter(last_name__contains = lastname)

#     #print(userprofile)
    
#     try:
#         with transaction.atomic():
#             for obj in userprofile:
#                 data = {
#                     "user" : obj.user.username,
#                     "first_name" : obj.first_name,
#                     "last_name" : obj.last_name,
#                     "age" : obj.age
#                 }
#                 response.append(data)
        
#         return JsonResponse({"validation":"success", "status":True, "data":response})
#     except Exception as e:
#         return JsonResponse({"validation":str(e), "status":False})

# def delete_by_id(request):
#     params = json.loads(request.body)

#     user_id = params.get("user_id")

#     try:
#         with transaction.atomic():
#             UserProfile.objects.get(id = user_id).delete()
#         return JsonResponse({"validation":"success", "status":True})
#     except Exception as e:
#         return JsonResponse({"validation":str(e), "status":False})



# def update_user_by_id(request):
#     params = json.loads(request.body)
#     print(params)

#     user = params.get("user")
#     first_name = params.get("first_name")
#     last_name = params.get("last_name")
#     age = params.get("age")

#     user_id = params.get("user_id")
#     old_user = UserProfile.objects.get(id = user_id)
#     print(old_user)

#     # try:
#     #     with transaction.atomic():

#     #         for (key, value) in params.items():
#     #             setattr(old_user, key, value)
#     #         old_user.save()
                

#     try:
#         with transaction.atomic():
            

#             user_profile = UserProfile.objects.filter(id = user_id).update(
#                 first_name =first_name,
#                 last_name = last_name,
#                 age = age
#             )
    
#         return JsonResponse({"validation":"success", "status":True})
#     except Exception as e:
#         return JsonResponse({"validation":str(e), "status":False})












