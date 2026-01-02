from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('product/', include('main.product.urls')),
    path('api/', include('main.orders.urls')),
    path('api/', include('main.Business.urls')),
    path('api/', include('main.service_section.Serviceproduct.urls')),
    path('api/', include('main.service_section.Payment.urls')),
    path('api/', include('main.service_section.Subject.urls')),
    path('api/', include('main.service_section.Serviceorder.urls')),
]
