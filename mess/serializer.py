from rest_framework import serializers

from mess.models import Mess, Menu, Price


class MessSerializer(serializers.ModelSerializer):
    """
    serialize Mess details
    """

    class Meta:
        model = Mess
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    """
    serialize Menu details
    """

    class Meta:
        model = Menu
        fields = "__all__"


class PriceSerializer(serializers.ModelSerializer):
    """
    serialize Menu details
    """

    class Meta:
        model = Price
        fields = "__all__"
