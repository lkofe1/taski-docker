from api import views
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.http import HttpResponse


def home_view(request):
    return HttpResponse("Taski API is running", status=200)


router = routers.DefaultRouter()
router.register('tasks', views.TaskView, 'task')

urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
