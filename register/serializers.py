from .models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('last_login', 'date_joined', 'is_active', 'is_shop', 'is_user', 'is_active'
                            'is_staff', 'is_superuser', 'groups', 'user_permissions')

        def create(self, validated_data):
            return Profile.objects.create(**validated_data)