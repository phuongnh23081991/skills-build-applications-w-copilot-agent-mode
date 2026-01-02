from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    @transaction.atomic
    def handle(self, *args, **options):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Team')
        dc = Team.objects.create(name='DC', description='DC Team')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, calories=300, date='2026-01-01')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=450, date='2026-01-02')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, calories=600, date='2026-01-03')
        Activity.objects.create(user=users[3], type='Yoga', duration=40, calories=200, date='2026-01-04')

        # Create workouts
        cardio = Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')
        strength = Workout.objects.create(name='Strength Training', description='Build muscle and strength')
        cardio.suggested_for.add(marvel, dc)
        strength.suggested_for.add(marvel, dc)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=750, rank=1)
        Leaderboard.objects.create(team=dc, points=650, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
