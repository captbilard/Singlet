from django.urls import path,include
from backend import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UsersViewSet)
# router.register(r'users/<int:pk>/', views.UserDetailViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    path('api/', include(router.urls))
]
