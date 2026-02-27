
from rest_framework.routers import DefaultRouter
from .views import WorkoutViewSet
from .views import UserViewSet

router = DefaultRouter()
router.register(r'workouts', WorkoutViewSet, basename='workouts')
router.register(r'users', UserViewSet, basename='users')
urlpatterns = router.urls
