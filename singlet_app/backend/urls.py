from django.urls import path,include
from backend import views
from rest_framework.urlpatterns import format_suffix_patterns
#from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'users', views.AdminUsersView)
# router.register(r'users/<int:pk>/', views.UserDetailViewSet)

urlpatterns = format_suffix_patterns([
    path('', views.index, name="index"),
    path('api/users/', views.UserList.as_view(), name='user-list'),
    path('api/users/<int:pk>/', views.UserDetails.as_view(), name='user-detail'),
    # path('api/users', views.UsersList.as_view())
    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
])
# urlpatterns = format_suffix_patterns(urlpatterns)