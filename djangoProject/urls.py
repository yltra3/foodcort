"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from food.views import (
    test,
    Restaurants,
    McDonaldsListView,
    HealthyFoodMenuView,
    BlinoffMenuView,
    McDonaldsOrderView,
)
from rest_framework import routers

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

restaurants_router = routers.SimpleRouter()
restaurants_router.register(r"restaurants", Restaurants)

McDonaldsOrder_router = routers.SimpleRouter()
McDonaldsOrder_router.register(r"order", McDonaldsOrderView)

urlpatterns = [
    # YOUR PATTERNS
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("admin/", admin.site.urls),
    path("", include(restaurants_router.urls)),
    path("restaurants/mcdonalds", McDonaldsListView.as_view()),
    path("restaurants/mcdonalds/", include(McDonaldsOrder_router.urls)),
    path("restaurants/healthyfood", HealthyFoodMenuView.as_view()),
    path("restaurants/healthyfood/order", HealthyFoodMenuView.as_view()),
    path("restaurants/blinoff", BlinoffMenuView.as_view()),
    path("1/", test),
]
