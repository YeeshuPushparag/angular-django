from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter
router =  SimpleRouter()
router.register('studentapi', views.StudentViewSet, basename='student')
urlpatterns = [
    path("", include(router.urls)),
    path("signup", views.signup, name="signup"),
    path("login", views.loginuser, name="login"),
    path("update", views.update, name="update"),
    path("logout", views.logoutuser, name="logout"),
]
