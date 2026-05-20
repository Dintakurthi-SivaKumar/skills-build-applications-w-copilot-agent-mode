from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='Easy'),
            Workout.objects.create(name='Running', description='Run 5km', difficulty='Medium'),
            Workout.objects.create(name='Deadlift', description='Deadlift 100kg', difficulty='Hard'),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Pushups', duration=20, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Deadlift', duration=40, date=timezone.now().date())

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=90)
        Leaderboard.objects.create(user=users[3], score=95)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
