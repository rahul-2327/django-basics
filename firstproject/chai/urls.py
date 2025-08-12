from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('<int:chai_id>/', views.chai_details, name='chai_details'),

]
