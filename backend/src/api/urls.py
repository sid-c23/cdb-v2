from django.urls import include, path
from rest_framework import routers

from users import views as users_views
from clubs import views as clubs_views

router = routers.DefaultRouter()
router.register('users', users_views.CustomUserViewSet)
router.register('clubs', clubs_views.ClubViewSet)
router.register('announcements', clubs_views.AnnouncementViewSet)

urlpatterns = [
		path('rest-auth/', include('rest_auth.urls')),
		path('rest-auth/registration/', include('rest_auth.registration.urls')),
		path('', include(router.urls))
]