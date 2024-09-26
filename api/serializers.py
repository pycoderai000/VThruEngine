from rest_framework import serializers
from . import models


class CartSerialzer(serializers.ModelSerializer):

    class Meta:
        model = models.Cart
        fields = ["id","cart_items"]




class CategorySerialzer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ["id","name"]