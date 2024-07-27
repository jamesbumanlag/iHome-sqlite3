
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('reset', views.reset, name='reset'),
    path('navbar', views.navbar, name='navbar'),
    path('logout_user', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('residents', views.residents, name='residents'),
    path('add_res', views.add_res, name='add_res'),
    path('record/<int:pk>', views.cus_record, name='record'),
    path('add_record', views.add_record, name='add_record'),
    path('update/<int:pk>', views.update_record, name='update'),
    path('delete/<int:pk>', views.delete_record, name='delete'),
    path('personal_care', views.personal_care, name='personal_care'),
    path('mobility', views.mobility, name='mobility'),
    path('view_care', views.view_care, name='view_care'),
    path('progress_notes', views.progress_notes, name='progress_notes'),
    path('nutrition', views.nutrition, name='nutrition'),
    path('health', views.health, name='health'),
    path('activities', views.activities, name='activities'),
    path('house', views.house, name='house'),
    
]