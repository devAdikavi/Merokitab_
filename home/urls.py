from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
   path('', views.home, name='home'),
   path('signup/', views.signup_view, name='signup_view'),
   path('login/', views.login_view, name='login_view'),
   path('logout/', views.logoutUser, name='logout'),
   path('add_product/', views.addproduct, name='add_product'),
   path('contact/', views.contactus, name='contactus'),
   path('prod_detail/<str:pk>/',views.prod_detail,name = 'prod_detail'),
   path('search',views.search,name = 'search'),
   path('userprofile',views.userprofile,name = 'userprofile'),
   path('category/<str:cats>/',views.category_view,name = 'category_view')

]