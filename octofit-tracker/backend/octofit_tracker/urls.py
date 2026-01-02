from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

@api_view(['GET'])
def api_root(request):
    return Response({
        'users': '/users/',
        'teams': '/teams/',
        'activities': '/activities/',
        'workouts': '/workouts/',
        'leaderboard': '/leaderboard/',
    })

urlpatterns = [
    path('', api_root, name='api_root'),
    path('', include(router.urls)),
]
