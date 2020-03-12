from rest_framework import serializers

from mess.models import Mess, Menu


class MessSerializer(serializers.ModelSerializer):
    """
    serialize Mess details
    """

    class Meta:
        model = Mess
        fields = "__all__"

    # @staticmethod
    # def get_price():
    #     return Menu.objects.select_related('price')


class MenuSerializer(serializers.ModelSerializer):
    """
    serialize Menu details
    """

    class Meta:
        model = Menu
        fields = "__all__"


