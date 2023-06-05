from django.urls import path, include
from rest_framework.routers import DefaultRouter

from epicevents.views import ClientViewSet, ContractViewSet, EventViewSet


router = DefaultRouter()
router.register(r"clients", ClientViewSet)
router.register(r"contracts", ContractViewSet)
router.register(r"events", EventViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
