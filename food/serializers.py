from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from food.models import Restaurants, HealthyFood, Blinoff, McDonaldsOrder
from food.models import McDonalds


class RestaurantsSerializer(ModelSerializer):
    class Meta:
        model = Restaurants
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = McDonaldsOrder
        fields = "__all__"


class OrderSerializerInput(ModelSerializer):
    class Meta:
        model = McDonaldsOrder
        fields = ["id", "name_id", "count", "price"]
        read_only_fields = ["id", "price"]


class McDonaldsSerializer(ModelSerializer):
    class Meta:
        model = McDonalds
        fields = "__all__"


class HealthyFoodSerializer(ModelSerializer):
    class Meta:
        model = HealthyFood
        fields = "__all__"


class BlinoffSerializer(ModelSerializer):
    class Meta:
        model = Blinoff
        fields = "__all__"
