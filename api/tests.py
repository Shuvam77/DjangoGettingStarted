# from django.test import TestCase
# from meetings.models import Meeting
# # Create your tests here.
#
#
# class MeetingTest(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         Meeting.objects.create(title='This Is Test!', date='2021-10-01', start_time='10:15:00', duration='4', organizer=1, room='1', comments=[])
#
#     def test_title_content(self):
#         meeting = Meeting.objects.get(id=1)
#         expected_object_name = f'{meeting.title}'
#         self.assertEqual(expected_object_name, 'This Is Test')
#
#     def test_date_content(self):
#         meeting = Meeting.objects.get(id=1)
#         expected_object_name = f'{meeting.date}'
#         self.assertEqual(expected_object_name, '2021-10-01')