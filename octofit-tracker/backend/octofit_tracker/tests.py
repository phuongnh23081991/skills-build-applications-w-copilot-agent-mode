from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=team)
        self.assertEqual(user.name, 'Spider-Man')
        self.assertEqual(user.team.name, 'Marvel')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='DC', description='DC Team')
        self.assertEqual(team.name, 'DC')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, calories=300, date='2026-01-01')
        self.assertEqual(activity.type, 'Running')
        self.assertEqual(activity.user.name, 'Iron Man')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        team = Team.objects.create(name='DC', description='DC Team')
        workout = Workout.objects.create(name='Cardio', description='Cardio workout')
        workout.suggested_for.add(team)
        self.assertEqual(workout.name, 'Cardio')
        self.assertIn(team, workout.suggested_for.all())

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        leaderboard = Leaderboard.objects.create(team=team, points=1000, rank=1)
        self.assertEqual(leaderboard.team.name, 'Marvel')
        self.assertEqual(leaderboard.rank, 1)
