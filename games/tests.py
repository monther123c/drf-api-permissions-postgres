from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import  status
# Create your tests here.
from django.contrib.auth import get_user_model
from .models import Game

from django.urls import reverse

class ThingTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass"
        )
        testuser2.save()

        test_game = Game.objects.create(
            name="pokemon",
            purchaser=testuser1,
            rank=10,
            description="pokemon GO!",
        )
        test_game.save()


    def setUp(self):
        self.client.login(username='testuser1', password="pass")




    def test_game_model(self):
        game = Game.objects.get(id=1)
        actual_purchaser = str(game.purchaser)
        actual_name = str(game.name)
        actual_description = str(game.description)
        actual_rank=10
        self.assertEqual(actual_purchaser, "testuser1")
        self.assertEqual(actual_name, "pokemon")
        self.assertEqual(
            actual_description, "pokemon GO!"
        )
        self.assertEqual(
            actual_rank, 10
        )

    def test_get_game_list(self):
        url = reverse("games_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        games = response.data
        self.assertEqual(len(games), 1)
        

    def test_auth_required(self):
        self.client.logout()
        url = reverse("games_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("games_detail", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
