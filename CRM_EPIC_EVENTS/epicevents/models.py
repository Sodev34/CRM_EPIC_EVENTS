from django.db import models
from authentication.models import EventStatus

from django.conf import settings


class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    company_name = models.CharField(max_length=25, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return f"Client {self.id} = {self.first_name} {self.last_name}"


class Contract(models.Model):
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )
    client = models.ForeignKey(
        to=Client, on_delete=models.SET_NULL, blank=True, null=True
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField(blank=True, null=True)
    payment_due = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Contract n°{self.id} : Seller {self.sales_contact.id} - Client {self.client.id}"


class Event(models.Model):
    contract = models.OneToOneField(
        to=Contract, on_delete=models.CASCADE, primary_key=True
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )
    event_status = models.ForeignKey(to=EventStatus, on_delete=models.PROTECT, default=1) 
    attendees = models.IntegerField(blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Event of contract {self.contract.id}  : Support {self.support_contact.id} "
