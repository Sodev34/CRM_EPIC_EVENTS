from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewSet, TeamViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"teams", TeamViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("login/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
