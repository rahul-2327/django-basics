from django.urls import path
from testapp import views


# url conf. module
urlpatterns = [
    path('hello', views.greeting),
    path('about', views.about),
    path('contact', views.contact),
]
