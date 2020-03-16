from rest_framework import serializers
from register.models import User,ShopOwner

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

class ShopSerializers(serializers.ModelSerializer):

    class Meta:
        model = ShopOwner
        fields = "__all__"