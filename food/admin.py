from django.contrib import admin

from food.models import Restaurants, McDonalds, HealthyFood, Blinoff, McDonaldsOrder

admin.site.register(Restaurants)
admin.site.register(McDonalds)
admin.site.register(HealthyFood)
admin.site.register(Blinoff)
admin.site.register(McDonaldsOrder)
