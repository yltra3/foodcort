from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Restaurants(models.Model):
    name = models.CharField(max_length=150, unique=True)
    healthy = models.CharField(max_length=150)
    max_people = models.IntegerField()

    def __str__(self):
        return self.name


class McDonalds(models.Model):
    menu_name = models.CharField(max_length=40)
    name = models.CharField(max_length=40, default="null", unique=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class McDonaldsOrder(models.Model):
    name_id = models.ForeignKey(McDonalds, on_delete=models.CASCADE)
    price = models.IntegerField()
    count = models.IntegerField()

    # @classmethod
    # def create_order(self, cls):
    #    return Order

    def __str__(self):
        return self.name_id


class HealthyFood(models.Model):
    type = models.CharField(max_length=40)
    name = models.CharField(max_length=40, unique=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Blinoff(models.Model):
    dough = models.CharField(max_length=40)
    name = models.CharField(max_length=40, unique=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name
