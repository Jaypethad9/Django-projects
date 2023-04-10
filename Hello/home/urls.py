from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
      path("",views.index,name='index'),
      path("shop",views.shop,name='shop'),
      path("home",views.home,name='home'),
      path("about",views.about,name='about'),
      path("login",views.login,name='login'),
      path("logout",views.logout,name='logout'),
      path("report",views.report,name='report'),
      path("search",views.search,name='search'),
      path("register",views.register,name='register'),
]
