from rest_framework import serializers

from .models import Client, Contract, Event
from authentication.models import User


class SalesPKField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        queryset = User.objects.filter(team_id=2)
        return queryset


class SupportsPKField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        queryset = User.objects.filter(team_id=3)
        return queryset


class ClientSerializer(serializers.ModelSerializer):
    sales_contact = SalesPKField()

    class Meta:
        model = Client
        fields = "__all__"
        ordering = ["id"]


class ContractSerializer(serializers.ModelSerializer):
    sales_contact = SalesPKField()

    class Meta:
        model = Contract
        fields = "__all__"
        ordering = ["id"]


class EventSerializer(serializers.ModelSerializer):
    support_contact = SupportsPKField()

    def validate_contract(self, contract):
        if not contract.status:
            raise serializers.ValidationError(
                "Cannot create event for a contract with not signed."
            )
        return contract

    class Meta:
        model = Event
        fields = "__all__"
        ordering = ["id"]
