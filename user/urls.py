from rest_framework import routers
from .views import UserViewSet, home
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

app_name='user'
urlpatterns = [
    path('api/', include((router.urls))),
    path('', home, name='home'),
]