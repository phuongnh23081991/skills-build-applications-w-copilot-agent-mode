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
    import os
    codespace_name = os.environ.get('CODESPACE_NAME', '')
    base_url = f"https://{codespace_name}-8000.app.github.dev/api" if codespace_name else "/api"
    return Response({
        'users': f'{base_url}/users/',
        'teams': f'{base_url}/teams/',
        'activities': f'{base_url}/activities/',
        'workouts': f'{base_url}/workouts/',
        'leaderboard': f'{base_url}/leaderboard/',
    })

urlpatterns = [
    path('', api_root, name='api_root'),
    path('', include(router.urls)),
]
