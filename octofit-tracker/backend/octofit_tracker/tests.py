from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, type='Test', duration=10, date=timezone.now().date())
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_user(self):
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.team.name, 'Test Team')

    def test_activity(self):
        self.assertEqual(self.activity.user, self.user)

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.user, self.user)

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Test Workout')
