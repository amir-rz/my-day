from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from . import models


class TestModels(TestCase):

    def test_todo_str_repr(self):
        """ Test todo string representation """
        todo = models.Todo.objects.create(title="Plan up for the next project")

        self.assertEqual(str(todo), todo.title)


TODOS_URL = reverse("todo:todo-list")


class TestAPIs(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_list_todos(self):
        """ Test list all existing todos """
        todo_item = sample_todo("Test todo item")
        res = self.client.get(TODOS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)


def sample_todo(title):
    """ Creates and returns a simple Todo instance """
    return models.Todo.objects.create(title=title)
