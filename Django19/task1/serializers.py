from rest_framework import serializers
from .models import Buyer, Game


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['id', 'username', 'balance', 'age']


class GameSerializer(serializers.ModelSerializer):
    # buyer = BuyerSerializer()  # Вложенный сериализатор

    class Meta:
        model = Game
        fields = ['id', 'title', 'cost', 'size', 'description', 'age_limited', 'buyer']
