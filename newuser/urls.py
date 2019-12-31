from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *



urlpatterns = [
    path('create_user_profile/',create_user_profile),
    path('create_address/',create_address),
    path('create_buyersprofile/',create_buyersprofile),
    path('create_sellersprofile/',create_sellersprofile),
    path('get_user_by_id/',get_user_by_id),
    path('get_address_by_id/',get_address_by_id),
    path('get_buyersprofile_by_id/',get_buyersprofile_by_id),
    path('get_sellersprofile_by_id/',get_sellersprofile_by_id),
    path('get_all_userprofile/',get_all_userprofile),
    path('get_all_buyersprofile/',get_all_buyersprofile),
    path('get_all_sellersprofile/',get_all_sellersprofile),
    path('update_userprofile_by_id/',update_userprofile_by_id),
    path('update_address_by_id/',update_address_by_id),
    path('login_view/',login_view),
    path('logout_view/',logout_view),
    path('change_password_view/',change_password_view),
    path('forget_password_view/',forget_password_view),
    path('signup/', views.SignUp.as_view(), name='signup'),
    # path('filter_by_first_name/',filter_by_first_name),
    # path('delete_by_id/',delete_by_id),
]
