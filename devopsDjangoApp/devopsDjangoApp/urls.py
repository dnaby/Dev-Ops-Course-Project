from django.contrib import admin
from django.urls import path, include
from devops_backend.views import getUsers, count_visits

urlpatterns = [
    path('users/', getUsers, name='user_list'),
    path('count-visits/', count_visits, name='count-visits'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
