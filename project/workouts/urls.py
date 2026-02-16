
from rest_framework.routers import DefaultRouter
from .views import WorkoutViewSet

router = DefaultRouter()
router.register(r'workouts', WorkoutViewSet, basename='workouts')

urlpatterns = router.urls
