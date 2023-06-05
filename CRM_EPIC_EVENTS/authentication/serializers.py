from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, Team, Statut


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "phone",
            "is_staff",
            "team",
        ]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name"]


class StatutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statut
        fields = ["id", "name"]
