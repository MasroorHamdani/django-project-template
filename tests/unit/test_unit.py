from django.test import TestCase
from todoapp.models import Task
from django.contrib.auth.models import User


#class TestAssertWorks(unittest.TestCase):
#   def test_assert_equals(self):
#       self.assertEquals(100, 100, '100 == 100')

#   def test_assert_true(self):
#       self.assertTrue(100 > 1, '100 > 1')


# Create your tests here.
class SectionTestCase(TestCase):
    def setUp(self):
        userid = User.objects.create(username="user1", password="user1")
        Task.objects.create(task_name="task1", task_desc="task1 desc",
                        task_status="open", created_on="2013-01-20",
                        task_priority="public", user=userid)

    def test_task_are_saved(self):
        userid = User.objects.get(username="user1")
        task = Task.objects.filter(user_id=userid)
        self.assertEqual(len(task), 1, 'the task was not saved')

    def test_status_for_all_task(self):
        resp = self.client.get('/all')
        self.assertEqual(resp.status_code, 200,
                         'all task retrieving code is not correct')

    def test_status_for_particular_user(self):
        resp = self.client.get('/index/1')
        self.assertEqual(resp.status_code, 200,
                         'task retrieval for particular user code not correct')