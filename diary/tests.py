import datetime
from django.test import TestCase
from .models import Diary

# Create your tests here.
class DiaryModelTests(TestCase):

    def test_diary_has_date(self):
        """
        Confirm whether created diary data has datetime
        """
        Diary.objects.create(title='test_title', text='test_text')
        actual_diary = Diary.objects.get(title='test_title')
        self.assertIsInstance(actual_diary.date, datetime.date)

    def test_save_and_retrieve(self):
        """
        confirm the save and retrieve of diary data
        """
        Diary.objects.create(title='test_title', text='test_text')
        actual_diary = Diary.objects.get(title='test_title')
        self.assertEqual(actual_diary.title, 'test_title')
