from django.urls import path
from real_estate_management_app import views


urlpatterns = [
    path("", views.index,name='index'),

    path("login_page", views.login_page,name='login_page'),

    path("register_page", views.register_page,name='register_page'),

    path("admin_home", views.admin_home,name='admin_home'),

    path("tenant_home", views.tenant_home,name='tenant_home'),

    path("tenantregister", views.tenantregister,name='tenantregister'),

    path("userlogin", views.userlogin,name='userlogin'),

    path("add_property_page", views.add_property_page,name='add_property_page'),

    path("admin_add_property", views.admin_add_property,name='admin_add_property'),

    path("admin_view_property", views.admin_view_property,name='admin_view_property'),

    path("admin_add_unit_page/<int:id>", views.admin_add_unit_page,name='admin_add_unit_page'),

    path("admin_add_unit/<int:pid>", views.admin_add_unit,name='admin_add_unit'),

    path("admin_view_unit/<int:id>", views.admin_view_unit,name='admin_view_unit'),

    path("tenant_view_more/<int:id>", views.tenant_view_more,name='tenant_view_more'),

    path("tenant_getnow_page/<int:id>", views.tenant_getnow_page,name='tenant_getnow_page'),

    path("tenant_add_rentdetails/<int:uid>", views.tenant_add_rentdetails,name='tenant_add_rentdetails'),

    path("tenant_profile", views.tenant_profile,name='tenant_profile'),



]