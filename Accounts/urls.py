# snippets/urls.py
from django.urls import path, include
from rest_framework import routers
from Accounts import views

router = routers.DefaultRouter()
router.register("cls", views.ClientList)
router.register("cls/acc", views.AccountList)


urlpatterns = [
    path('client/', views.ClientList.as_view()),
    path('account/', views.AccountList.as_view()),
]
