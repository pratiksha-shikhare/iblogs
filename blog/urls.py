# manual urls.py file of blog app
# from django.contrib import admin
from django.urls import path,include
# from django.conf.urls.static import static  # ethun static method yete i.e use karto hya inbuilt pkg mdun
# from django.conf import settings  #ethun settings import karat aahe
from .views import home,post,category

urlpatterns = [
    path('home', home),
    path('blog/<slug:url>',post),
    path('category/<slug:url>',category)
    
]