from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView

from food.models import Restaurants, HealthyFood, McDonalds, Blinoff, McDonaldsOrder
from rest_framework.response import Response
from .serializers import (
    McDonaldsSerializer,
    RestaurantsSerializer,
    HealthyFoodSerializer,
    BlinoffSerializer,
    OrderSerializer,
    OrderSerializerInput,
)


def test(request):
    capitals = Restaurants.objects.all()
    print(capitals)
    return render(request, "test.html")


class Restaurants(viewsets.ModelViewSet):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer
    # def get(self, request):
    #     """
    #     Контроллер для отображения на главной странице списка всех записей.
    #     """
    #     r = Restaurants.objects.all()
    #     return Response(data=RestaurantsSerializer(r, many=True).data)


class McDonaldsListView(APIView):
    def get(self, request):
        menu = McDonalds.objects.all()
        return Response(data=McDonaldsSerializer(menu, many=True).data)

    def post(self, request):
        serializer = McDonaldsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_new = McDonalds.objects.create(
            menu_name=serializer.validated_data["menu_name"],
            name=request.data["name"],
            price=request.data["price"],
        )
        return Response(model_to_dict(post_new))


class McDonaldsOrderView(viewsets.ModelViewSet):
    # def get(self, request):
    #     menu = McDonaldsOrder.objects.all()
    #     return Response(data=OrderSerializer(menu, many=True).data)
    queryset = McDonaldsOrder.objects.all()
    serializer_class = OrderSerializerInput

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # mc = McDonalds.objects.get(pk=serializer.validated_data["name_id"].pk)
        new_order = McDonaldsOrder.objects.create(
            **serializer.validated_data,
            price=serializer.validated_data["name_id"].price
            * serializer.validated_data["count"]
        )
        headers = self.get_success_headers(OrderSerializerInput(new_order).data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
    # def post(self, request):
    #     if isinstance(request.data, list):
    #         for value in request.data:
    #             serializer = OrderSerializerInput(data=value)
    #             serializer.is_valid(raise_exception=True)
    #             McDonaldsOrder.objects.create\
    #                 (name_id=serializer.validated_data["name_id"],
    #                  count=value["count"],
    #                  price=McDonaldsSerializer(McDonalds.objects.get(id=value["name_id"])).data["price"])
    #     elif isinstance(request.data, dict):
    #         serializer = OrderSerializerInput(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         McDonaldsOrder.objects.create\
    #             (name_id=serializer.validated_data["name_id"],
    #              count=request.data["count"],
    #              price=McDonaldsSerializer(McDonalds.objects.get(id=request.data["name_id"])).data["price"])
    #     return Response(data=OrderSerializer(McDonaldsOrder.objects.all(), many=True).data)


class HealthyFoodMenuView(APIView):
    def get(self, request):
        menu = HealthyFood.objects.all()
        return Response(data=HealthyFoodSerializer(menu, many=True).data)


class BlinoffMenuView(APIView):
    def get(self, request):
        menu = Blinoff.objects.all()
        return Response(data=BlinoffSerializer(menu, many=True).data)
