from django.contrib import admin
from django.urls import path
from devops_backend.views import getUsers, count_visits

urlpatterns = [
    path("get_users/", getUsers, name="get all users"),
    path("count_visits/", count_visits, name="count number of visits"),
    path("admin/", admin.site.urls),
]
