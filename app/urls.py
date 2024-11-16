from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
        path('', views.index, name='index'),
        path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
        path('service-details/', views.service_details, name='service-details'),
]